# ch4_14_foreign_key

## Foreign Key

![Untitled](ch4_14_foreign_key%203f9352b1e2f94bc88871b316eb83ea00/Untitled.png)

지난 시간에 다뤘던 reviews 테이블은 items 테이블의 id 값을 자신의 컬럼으로 가지면서 1:N 관계를 맺는다고 배웠습니다. 즉, 하나의 아이템이 여러개의 리뷰를 갖게 되는 구조입니다. reviews 테이블의 item_id 값을 보고, 어느 아이템에 달린 리뷰인지를 알 수 있었습니다. 

그런데 items 테이블에 있지도 않은 id 값을 가진 review가 reviews 테이블에 insert 되면 어떨까요? 이는 우리가 의도한 방식을 벗어난 예외 상황이 되겠죠? 이를 방지하기 위해서 RDBMS에서는 foreign key라는 장치를 제공하고 있습니다.

### Foreign Key 생성하기

```sql
ALTER TABLE "테이블 명"
ADD CONSTRAINT "foreign key 이름"
FOREIGN KEY ("foreing key를 걸 컬럼") REFERENCES "참조 받는 테이블"("참조 컬럼");
```

```sql
ALTER TABLE reviews
ADD CONSTRAINT FK_reviews_item_id
FOREIGN KEY (item_id) REFERENCES items(id);
```

foreign key 를 생성한 다음, items 테이블의 id 값에 존재하지 않는 값을 갖는 review를 추가해보면 foreign key 조건을 위배했다고 실패합니다.

![Untitled](ch4_14_foreign_key%203f9352b1e2f94bc88871b316eb83ea00/Untitled%201.png)

### Foreign Key ON DELETE CASCADE

특정 item이 items 테이블에서 삭제되었다고 가정해보겠습니다. 이 때, item은 사라졌는데 review는 그대로 남아있으면 어색하겠죠? item이 사라질 때, 이를 참조하는 review들도 함께 사라지도록 foreign key에 CASCADE라는 옵션을 줄 수 있습니다. 이는 참조하는 컬럼 값이 업데이트 되거나 삭제 될 때, 이를 참조하는 테이블에도 반영해달라는 의미입니다.

먼저 기존의 foreign key를 DROP 하고, 새로 만들어보겠습니다.

```sql
ALTER TABLE reviews
DROP FOREIGN KEY FK_reviews_item_id;
```

```sql
ALTER TABLE reviews
ADD CONSTRAINT FK_reviews_item_id
FOREIGN KEY (item_id) REFERENCES items(id)
ON DELETE CASCADE;
```

### Foreign Key ON UPDATE CASCADE

update도 마찬가지입니다. items 테이블의 특정 레코드의 id 컬럼 값이 업데이트가 되었는데, 이를 참조하는 reviews 테이블에 반영되지 않으면 JOIN은 수행할 수가 없어져 버립니다. 다만, 실제로는 primary key의 값 자체가 update 되는 상황이 발생하는 상황은 거의 없어서 잘 사용하지 않습니다.

기존 FOREIGN KEY를 DROP하고  ON UPDATE CASCADE 까지 추가해서 Foreign key를 만들어 보겠습니다. 

```sql
ALTER TABLE reviews
DROP FOREIGN KEY FK_reviews_item_id;
```

```sql
ALTER TABLE reviews
ADD CONSTRAINT FK_reviews_item_id
FOREIGN KEY (item_id) REFERENCES items(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

## 정리

foreign key는 RDBMS에 저장되는 데이터들의 무결성(integrity)를 보장하기 위한 일종의 제약 조건입니다. 제약 조건을 걸어주는 것이기 때문에 부하가 발생해서 트래픽이 높거나 데이터의 읽기, 쓰기 작업이 빈번한 DB에서는 처음에는 foreign key를 걸어주었다가도 제거하기도 합니다.