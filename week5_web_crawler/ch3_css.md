# ch3_css

## CSS

Cascading Style Sheets의 약자로 HTML 문서에 각종 디자인을 적용하기 위해 사용되는 언어입니다. HTML 태그에 id 혹은 class를 부여해서 적용할 수 있습니다. 별도의 css 파일을 만들고, 이를 HTML 태그의 head 태그 안에서 연결해서 사용합니다.

```html
<html>
  <head>
    <title>Todo App</title>
		<link rel="stylesheet" type="text/css" href="styles.css">
  </head>
  <body>
		<p>hello world</p>
	</body>
</html>
```

```css
p {
  background-color: red;
}
```

![Untitled](ch5_3_css%206aa037510d2c4ec7bbb81e4fd67d5bb3/Untitled.png)

위 예제에서는 html 파일에서 link 태그를 이용해 styles.css 파일을 연결했습니다. 그리고 styles.css 파일 안에는 p 태그의 배경색을 빨간색으로 지정하라는 코드가 담겨있습니다. 

### id를 이용해서 스타일 적용하기

자, 지난 시간에 코딩한 todo.html이 있다고 가정하겠습니다. CSS를 적용하지 않은 상태에서는 아래 스크린 샷 처럼 생겼습니다.

```html
<html>
  <head>
    <title>Todo App</title>
		<link rel="stylesheet" type="text/css" href="styles.css">
  </head>
  <body>
		<div>
      <h1>Todo App</h1>
			<p>2023 multicampus data analytics camp</p>
			<p>week5 web crawling</p>
      <input type="text" placeholder="Enter a task">
      <button>Add</button>
      <ul>
        <li class="todo-item">웹 크롤러 개념 강의 복습하기</li>
        <li class="todo-item">html 코딩 연습하기</li>
        <li class="todo-item">SQL 프로젝트 진행하기</li>
      </ul>
    </div>
	</body>
</html>
```

![Untitled](ch5_3_css%206aa037510d2c4ec7bbb81e4fd67d5bb3/Untitled%201.png)

먼저 div에 id 값을 부여해서 가운데 정렬을 구현해보겠습니다. css 파일에서 특정 id 값에 스타일을 부여할 때는 맨 앞에 #을 붙이면 됩니다. 내부에 포함된 요소들을 가운데 정렬 하기 위해서 text-align: center 라는 속성과 위에 약간의 여백을 주기 위해 margin-top 이라는 속성을 부여해보겠습니다. (여기서는 id 값을 부여해서 CSS를 적용하는 방법만 알면 됩니다. CSS 세부 내용은 몰라도 무방합니다.)

```html
<html>
  <head>
    <title>Todo App</title>
		<link rel="stylesheet" type="text/css" href="styles.css">
  </head>
  <body>
		<div **id="todo-container"**>
      <h1>Todo App</h1>
			<p>2023 multicampus data analytics camp</p>
			<p>week5 web crawling</p>
      <input type="text" placeholder="Enter a task">
      <button>Add</button>
      <ul>
        <li class="todo-item">웹 크롤러 개념 강의 복습하기</li>
        <li class="todo-item">html 코딩 연습하기</li>
        <li class="todo-item">SQL 프로젝트 진행하기</li>
      </ul>
    </div>
	</body>
</html>
```

```css
#todo-container {
	text-align: center;
	margin-top: 20px;
}
```

![Untitled](ch5_3_css%206aa037510d2c4ec7bbb81e4fd67d5bb3/Untitled%202.png)

가운데 정렬이 쫙 맞춰져서 보기 좋아졌습니다. 이번에는 과정명과 과목명을 나타내는 p 태그의 여백과 텍스트 색상을 변경해보겠습니다.

```html
...
			<p id="program-name">2023 multicampus data analytics camp</p>
			<p id="program-course">week5 web crawling</p>
...
```

```css
...

#program-name {
	margin: 5px;
	color: #037bfc;
	font-weight: bold;
	font-size: 20px;
}

#program-course {
	margin: 5px;
	color: #5886b8;
	font-size: 18px;
}
```

![Untitled](ch5_3_css%206aa037510d2c4ec7bbb81e4fd67d5bb3/Untitled%203.png)

과정명과 과목명에 각각 스타일을 부여하기 위해 id 값을 부여했습니다. 여백을 조절하기 위해서 margin이라는 값을 조정했습니다. 그리고 텍스트의 크기와 두께를 조정하기 위해 font-size와 font-weight 값을 조정했고, 색깔을 변경하기 위해 color에 직접 색상의 hexacode를 부여했습니다.

마지막으로 ul 태그에 id를 적용해서 각각의 li 태그 앞에 붙는 · 를 떼주겠습니다. list-style-type: none 이라는 속성을 부여해주면 됩니다.

```html
...
<ul id="todo-list">
	...
</ul>
...
```

```css
...
#todo-list {
  list-style-type: none;
}
```

![Untitled](ch5_3_css%206aa037510d2c4ec7bbb81e4fd67d5bb3/Untitled%204.png)

 

이처럼 id 값을 부여해서 스타일을 적용하는 것은 특정 element가 HTML 문서 내에서 유일할 때 많이 사용하는 기법입니다. 이는 크롤러를 개발할 때, 수집한 HTML 문서를 파싱할 때, 매우 유용하게 사용되니 꼭 기억해두시기 바랍니다.

### class를 이용해서 스타일 적용하기

여러 element들에 동시에 스타일을 적용하고 싶다면 class를 이용하는게 좋습니다. 위 todo app 예시에서는 각각의 todo item들이 반복적으로 등장합니다. 이들에게 동시에 스타일을 적용하고 싶다면 class를 부여하면 됩니다.

```html
...
<ul id="todo-list">
  <li class="todo-item">웹 크롤러 개념 강의 복습하기</li>
  <li class="todo-item">html 코딩 연습하기</li>
  <li class="todo-item">SQL 프로젝트 진행하기</li>
</ul>
...
```

```css
.todo-item {
  margin: 5px auto;
  width: 500px;
  padding: 10px;
  border: 1px solid #ccc;
  background-color: #e3f1ff;
}
```

![Untitled](ch5_3_css%206aa037510d2c4ec7bbb81e4fd67d5bb3/Untitled%205.png)

클래스에 CSS를 부여하고 싶다면 클래스 명 앞에 .을 붙여주면 됩니다. 여기서는 todo-item이라는 클래스에 여백과 너비, 배경색과 테두리를 부여했습니다. 특히 margin: 5px auto라는 속성이 살짝 까다로운데, 이는 위아래 여백은 5px, 좌우 여백은 알아서 자동으로 주어 가운데 정렬하라는 얘기입니다. 

CSS를 잘 코딩하는 것이 이번 과정에서는 중요하지 않기 때문에 별도로 CSS 코딩의 숙련도를 높이는 과제는 수행하지 않고 넘어가도록 하겠습니다. id와 class를 이용해서 CSS를 부여한다는 웹 프론트엔드 개발의 특징만 기억하고 넘어가면 됩니다.

## 정리

이번 챕터에서 다룬 것 외에도 유저 디바이스 크기에 따른 반응형 UI 디자인, flex 레이아웃 등 CSS는 정말 방대한 내용들이 있습니다. 우리는 웹 개발 수업이 아니기 때문에 id 값과 class 값을 부여해서 CSS를 적용한다는 내용만 숙지하고 넘어가도록 하겠습니다.