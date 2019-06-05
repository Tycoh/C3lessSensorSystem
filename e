[33mcommit 08fe700404eb60f610dd5f4d565517f4bdc21877[m[33m ([m[1;36mHEAD -> [m[1;32mpatch[m[33m, [m[1;31morigin/patch[m[33m)[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Fri May 31 10:04:50 2019 +0900

    fix:typo

[33mcommit ed7a57ce9b9ab92e2bf100fb1ffc610a8c3a8c8b[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Wed May 29 17:32:33 2019 +0900

    calcDataのエラー文のファイル名を修正

[33mcommit 69c1c5de63627bb541c668bf022023f70c6c57c3[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Wed May 29 17:29:52 2019 +0900

    デバッグレベルで読み込んだ認証ファイルを出力

[33mcommit 97029b51f1c6f683da918b55b91e3b91959dd0ad[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Wed May 29 17:26:28 2019 +0900

    AWS IoTのみを使うとき、sensor-data.ymlが読み込まれていないことを原因とするエラーを修正

[33mcommit 43857764cb54ef58ff877617ef545fcddce78074[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Wed May 29 17:21:56 2019 +0900

    1. getPathで、フォルダが空のときのエラーを追加
    2. sensorSystemの、リストを修正

[33mcommit f4856108db62a39a2ec5673793e06f2477c5ec2f[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Wed May 29 16:08:09 2019 +0900

    certicificate ファイルが見つからなかったときのエラー文を追加

[33mcommit 4b7fc9e6b9bf3865466e4f54e0eca76275734437[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Wed May 29 15:57:09 2019 +0900

    '/'を追加

[33mcommit fb62986418bbffb28625b13f5d9d70c531984e7f[m
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Tue May 28 16:17:32 2019 +0900

    Update README.md

[33mcommit 333f629155490e2619dd73e71a99dd9cd1f29515[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Mon May 27 17:38:21 2019 +0900

    READMEを修正

[33mcommit 7a489ef061e891595d2fee9e420957f06f68895d[m
Merge: 55a5901 7cebfc3
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Fri May 17 15:06:20 2019 +0900

    Merge branch 'master' of github.com:Tycoh/C3lessSensorSystem

[33mcommit 7cebfc30bccb119c17f7da3d9accff3cb82f8cb1[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Fri May 17 00:19:51 2019 +0900

    raise KeyError if sensor is not registered

[33mcommit dc0ea5c489683693b3104e6cc9fd326d57c8f12f[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Thu May 16 23:07:32 2019 +0900

    changed log message

[33mcommit 3b71cb46822f3e1ef5e1f6044f2727eccc66a27d[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Thu May 16 23:06:11 2019 +0900

    add comment

[33mcommit ea14436146a6f136c7748417efd185267f5a40ac[m
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Thu May 16 22:53:40 2019 +0900

    Update issue templates

[33mcommit f9e91a54b81e9e7a6ecb0a42ba98438dfe3bc300[m
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Thu May 16 22:47:01 2019 +0900

    不具合報告フォームを日本語化

[33mcommit 3be6c9a8360d5835113d941ee9eae48577196706[m
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Thu May 16 17:28:49 2019 +0900

    Update issue templates

[33mcommit 55a5901f66149bb660840063a757f685e3d1001f[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Wed May 15 16:07:15 2019 +0900

    added exfat install

[33mcommit ae6e476b1831e1fd6b5085206613b7848fe6e17c[m
Merge: 698b12a d944a0f
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Tue May 14 11:55:16 2019 +0900

    Merge pull request #5 from Tycoh/Tycoh-patch-1
    
    fixed link

[33mcommit d944a0fe644281b18a950cad4fd46c6375deac63[m[33m ([m[1;31morigin/Tycoh-patch-1[m[33m)[m
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Tue May 14 11:54:02 2019 +0900

    fixed link
    
    sshのリンクをhttpsに修正

[33mcommit 698b12aab3451cd54191ea1f0b191ef3016fdccf[m
Merge: 789155b 8fc1408
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Tue May 14 11:51:12 2019 +0900

    Merge pull request #4 from Tycoh/develop
    
    下記の点を修正
    1.gitでの管理に伴うディレクトリ構造の変化を反映
    2. ログにファイル名を追加
    3. SerialPortに関するエラーがログに出力されない問題を修正
    4. デフォルト設定を変更
    5. その他、軽微な修正

[33mcommit 8fc14083ae9edf2edaa45b31896488d4be8a78b5[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 11:45:01 2019 +0900

    fixed save directly

[33mcommit 1b9d91cfaea75379884e620c1bbd76df6fa0dffc[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 11:26:35 2019 +0900

    log before close serial port

[33mcommit a3f1c3800119cc4bddc251d74391ddba109e0c13[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 11:24:11 2019 +0900

    log serial port error

[33mcommit 1d4ffd14e092bee362ab881fa184e7159ded36a1[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 11:04:23 2019 +0900

    fixed SensorDefinisionYAML

[33mcommit 6c2fca5ab5456271cc5c35a39360d720ae5e48e2[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 11:01:08 2019 +0900

    changed default settings

[33mcommit f4c51c01ec4e01636ab019c35be854e9fc271bfd[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 10:59:04 2019 +0900

    fixed log filename

[33mcommit a2e1602a9afe43446c5204b35b18306d3c9c9e04[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 10:55:07 2019 +0900

    fixed service

[33mcommit ed37cc7eed145acacd406177da3020f4000c48a2[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 10:53:35 2019 +0900

    fixed setting yaml path

[33mcommit 92ca15c6b44159580dbd50990d29d04a7c9f1cc4[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 10:52:31 2019 +0900

    deleted yaml path

[33mcommit 98eb278ab5953624a1f404057709d5899c960af7[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 10:50:13 2019 +0900

    added log dir

[33mcommit e4c1205ae8cb7540daa9de531152f64563698af5[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 10:46:27 2019 +0900

    deleted apt upgrade

[33mcommit 0b9af652228e5bd1b246a7e5de287b6c133ca648[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 10:46:08 2019 +0900

    fixed dir

[33mcommit 789155b255cf0379e615da6d45cabc0cdb0f69e2[m
Merge: 647eb49 8588d2d
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Tue May 14 10:35:53 2019 +0900

    Merge pull request #2 from Tycoh/develop
    
    ファイルの依存関係の修正
    ローカルに書き込むデータに、子機の電源電圧を追加

[33mcommit 8588d2d0c640b9be110b0b650fd30fc11b04a8c1[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 10:33:38 2019 +0900

    fixed dir

[33mcommit 63c3d3f8ae4a2e7591433ce48276a9d8671f386a[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 10:31:14 2019 +0900

    added PS Voltage

[33mcommit 647eb49f0e05b67acbc66043983a993cf7b723a5[m
Merge: d8da496 0adc3f8
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Tue May 14 10:07:41 2019 +0900

    Merge pull request #1 from Tycoh/develop
    
    add quick start

[33mcommit 0adc3f8749a34bbe99ae053e03087cf2836ca4c4[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 09:58:23 2019 +0900

    add quick start

[33mcommit d8da4966654405e4779d71ec78352420fe9699dd[m
Author: Tetsuro <tetsuro.maruta@tycoh.co.jp>
Date:   Tue May 14 09:53:46 2019 +0900

    first commit

[33mcommit a88a2a49c9846f58b7af24ef8debb2c7f2e5a2e6[m
Author: Tycoh <40817973+Tycoh@users.noreply.github.com>
Date:   Tue May 14 09:51:50 2019 +0900

    Initial commit
