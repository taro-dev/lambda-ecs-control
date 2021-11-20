# lambda-ecs-control

## 使い方

AWS Lambdaから関数を新規作成

（※ランタイム：Python3.9）

コードソースへlambda.pyの内容を貼り付ける

```
L6 増減対象のクラスター名、サービス名を指定（複数指定可能）
L10 desiredCountへ変更後のタスク数を指定

０　⇨ 停止
１　⇨ 実行タスク数を１
```

## 定期実行

AWS EventBridge へルールを追加

UTCで指定が必要なので、曜日指定の場合は注意

cron(00 11 ? * MON-FRI *)　→ 平日20時に実行
