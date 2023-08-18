# apiros3 ブログページ

ブログを書いたり、保管したりする用    
特に複雑なことしてないので、実はクローンしたら同じ感じのブログを一瞬で生成できます！いい話

## 初期化
もしクローンして、自分用に変えたい！って思った場合は以下の数点の変更をお願いします：   
・html内のgithub, twitterアイコンのリンク先    
・HPタイトル     
・blog-mdの中身のmdファイルの削除    

その上で、
```powershell
  python blogify.py
```
を呼ぶとビルドします(ついでにblog-htmlの余分なファイルを削除してくれます)。   
mdファイルをblog-mdの中にいれてビルドすると出来上がりますし、github actionsにmain.ymlを突っ込めばmainにpushするたびにビルドしてくれます！

どこかのタイミングで上のこれを自動化できるpythonコード書いてもいいかな～とか思ってたりもします。
