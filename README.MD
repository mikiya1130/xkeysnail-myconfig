# xkeysnail-myconfig

xkeysnail設定用ファイル(自分用)

## 環境

- Ubuntu 20.04
- HHKB Professional2(US配列)

## 手順

```
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ ansible-galaxy install pddg.xkeysnail --roles-path roles/
(venv) $ ansible-playbook setup.yml -K
(venv) $ deactivate
$ shutdown -r now
```

## config.py 参考サイト

- https://github.com/mooz/xkeysnail
- https://poyo.hatenablog.jp/entry/2018/06/23/020147
