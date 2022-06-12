import subprocess
from subprocess import PIPE
import os
# coding: utf-8
# Your code here!
print('このプログラムはLinux専用です。')
print('管理者権限で実行してください。')
print('どうも、こんにちは\nここではVPSなどでマインクラフトのDOS、DDOS対策などのプロキシ設定を支援するものです。\n※このプログラムで問題が発生しても責任は負いません。')
print('説明ファイルはaboutフォルダのabout.txtの形式で保存しています。')

# 同意するか？
def yes_no_input():
    while True:
        choice = input("どちらですか？（以下のやり方で答えて下さい。） 'yes' か 'no' [y/N]: ").lower()
# ある場合
        if choice in ['y', 'ye', 'yes']:
            return True
# ない場合
        elif choice in ['n', 'no']:
            print('中断！')
            return False


if __name__ == '__main__':
    if yes_no_input():
        print('続けます。')

# apt インストール同意するか？
def yes_no_input():
    while True:
        choice = input("Nginx UFWを入れますがよろしいでしょうか？（以下のやり方で答えて下さい。） 'yes' か 'no' [y/N]: ").lower()
# ある
        if choice in ['y', 'ye', 'yes']:
            return True
# ない
        elif choice in ['n', 'no']:
            print('中断！')
            return False


if __name__ == '__main__':
    if yes_no_input():
        print('続けます。')
        
print('ここではaptを使います。CentOSではデフォルトではないので（だと思うので）/n yum install apt などでaptを入れてください。')

# apt入れた？
def yes_no_input():
    while True:
        choice = input("Aptを入れましたか？（以下のやり方で答えて下さい。） 'yes' か 'no' [y/N]: ").lower()
# ある
        if choice in ['y', 'ye', 'yes']:
            return True
# ない
        elif choice in ['n', 'no']:
            print('中断！')
            return False


if __name__ == '__main__':
    if yes_no_input():
        print('続けます。')
# ディレクトリ削除・ファイル削除
        res = subprocess.call("sudo rm -r /home/nginx", shell=True)
        res = subprocess.call("rm -r nginx-1.18.0.tar.gz", shell=True)
        res = subprocess.call("rm -r nginx-1.18.0/", shell=True)
# ファイル上書き
        inipporthea = open("data/file/inipport.txt","w")
        inipporthea.write("server ")
        inipporthea.close()
# コマンド実行
        print('NginxとUfwを入れます。')
        res = subprocess.call("sudo apt update && sudo apt upgrade -y", shell=True)
        res = subprocess.call("sudo apt install gcc", shell=True)
        res = subprocess.call("sudo apt install build-essential -y", shell=True)
        res = subprocess.call("wget https://nginx.org/download/nginx-1.18.0.tar.gz", shell=True)
        res = subprocess.call("tar -zxvf nginx-1.18.0.tar.gz", shell=True)
#        res = subprocess.call("cd nginx-1.18.0", shell=True)
        res = subprocess.call("cd nginx-1.18.0/ && ./configure --with-stream --without-http_rewrite_module --without-http_gzip_module", shell=True)
        res = subprocess.call("cd nginx-1.18.0/ && make", shell=True)
        res = subprocess.call("cd nginx-1.18.0/ && sudo make install", shell=True)
# Nginx設定ファイル変更
# 聞く
        sshportnum = input("SSHのポートを入力してください。（例：22）")
        outportnum = input("出力先のポートを入力してください。（例：25565）")
# ポート テキスト保存
        sshportfile = open("data/file/sshportfile.txt", 'a') 
        outportfile = open("data/file/outportfile.txt", 'a')
        sshportfile.write((sshportnum))
        outportfile.write((outportnum))
        sshportfile.close()
        outportfile.close()
# UFWコマンド＋ポート 変数格納
        ufwsshportfile = open('data/file/sshportfile.txt', 'r') 
        ufwoutportfile = open('data/file/outportfile.txt', 'r')
# コマンド実行
        res = subprocess.call(ufwsshportfile, shell=True)
        res = subprocess.call(ufwoutportfile, shell=True)
        res = subprocess.call("sudo ufw enable", shell=True)
        res = subprocess.call("sudo ufw reload", shell=True)
# sshportfile.txt・outportfile.txt ファイルリセット
        sshreset = open("data/file/sshportfile.txt", 'w') 
        outreset = open("data/file/outportfile.txt", 'w')
        sshreset.write("sudo ufw allow ")
        outreset.write("sudo ufw allow ")
        sshreset.close()
        outreset.close()
# ディレクトリ・ファイル作成
        os.makedirs('/home/nginx')
        inipportpath = '/home/nginx/in.conf'
        outipportpath = '/home/nginx/out.conf'
        indi = open(inipportpath, 'w')
        indi.write('')  # 
        indi.close()

        outdi = open(outipportpath, 'w')
        outdi.write('')  # 
        outdi.close()
# IP聞く・上書き
        inip = input("マイクラサーバーのグローバルサーバーIPもしくはプライベートIP（同じネットワーク上のみ）を入力してください。（グローバルIPの場合の例：182.22.25.124(Yahho)プライベートIPの場合の例：192.168.0.10）")
#        inipport = open('data/file/inipport.txt','a')
#        inipport.write((inip))
#        inipport.write(":")
#        inipport.close()
        inportf = input("マイクラサーバーのポートを入力してください。（例：25565）")
#        inipporttwo = open('data/file/inipport.txt','a')
#        inipporttwo.write((inport))
#        inipporttwo.write(";")
#        inipporttwo.close()
#        inipporthe = open('data/file/inipport.txt','r')
# 入力ポート・出力ポート保存ファイル上書き
        infi = open('/home/nginx/in.conf','a')
        infi.write("server "+str(inip)+":"+str(inportf)+";")
        infi.close()

#        infitwo = open('/home/nginx/in.conf','a')
#        infitwo.write(":", (inport), ";")
#        infitwo.close()        


        outfi = open('/home/nginx/out.conf','w')
        outfi.write("listen     "+str(outportnum)+"; \n proxy_pass mcserver;")
        outfi.close()
# Nginxファイル変更（警告も）
def yes_no_input():
    while True:
        choice = input("Nginxファイル(/etc/nginx/nginx.conf)を変更しますがよろしいでしょうか？（以下のやり方で答えて下さい。） 'yes' か 'no' [y/N]: ").lower()
# OK
        if choice in ['y', 'ye', 'yes']:
            return True
# NO
        elif choice in ['n', 'no']:
            print('中断！')
            return False


if __name__ == '__main__':
    if yes_no_input():
        print('続けます。')
# nginx.conf上書き
        nginxsamplefile = open('data/nginxfile/nginx.conf', 'r') 
        contents = nginxsamplefile.read()
        nginxfile = open('/usr/local/nginx/conf/nginx.conf','w')
        nginxfile.write(str(contents))
        nginxfile.close()
        nginxsamplefile.close()
# nginx.service作成＆上書き
        nginxservicesamplefile = open('data/file/nginx.service', 'r') 
        servicecontents = nginxservicesamplefile.read()
        nginxservicefile = open('/usr/lib/systemd/system/nginx.service','w')
        nginxservicefile.write(str(servicecontents))
        nginxservicefile.close()
        nginxservicesamplefile.close()
# Nginx再起動
        res = subprocess.call("sudo systemctl daemon-reload", shell=True)
        res = subprocess.call("sudo systemctl restart nginx", shell=True)
        res = subprocess.call("sudo systemctl status nginx", shell=True)
# 終わりの通知・設定の変更方法など
        print('設定が終わりました。（正常の場合）\n もし設定を変更したい場合は/etc/nginx/nginx.conf（Nginx本体ファイル）/home/nginx/out.conf（プロキシ出力ポートファイル）/home/nginx/in.conf（マイクラサーバー入力側IP・ポートファイル）') 
# 終わり
        print('ご利用ありがとうございます。またのご利用お待ちしております！ \n Solo-Thunder')
    
        
