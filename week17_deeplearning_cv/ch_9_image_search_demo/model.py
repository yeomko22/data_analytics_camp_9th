from torchvision.models import resnet18, ResNet18_Weights
import torch


class EmbeddingExtractor:
    def __init__(self, weight_path=None):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # load model
        self.model = resnet18()
        self.model.fc = torch.nn.Linear(in_features=512, out_features=12)
        if weight_path:
            self.model.load_state_dict(torch.load(weight_path, map_location=self.device))
        self.model = self.model.to(self.device)
        self.model.eval()

        # preprocess logic
        self.transform = ResNet18_Weights.IMAGENET1K_V1.transforms()

        # register hook
        self.intercepted_embedding = None

        def _hook_fn(module, input, output):
            embedding = torch.flatten(output, start_dim=1).cpu().tolist()[0]
            self.intercepted_embedding = embedding
        self.hook = self.model.avgpool.register_forward_hook(_hook_fn)

    def extract_features(self, image):
        image_tensor = self.transform(image).to(self.device)
        with torch.no_grad():
            outputs = self.model(image_tensor.unsqueeze(0))
        probs = torch.nn.functional.softmax(outputs[0], dim=0)
        pred = torch.argmax(probs).item()
        return pred, self.intercepted_embedding
