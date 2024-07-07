import streamlit as st
import time
from datetime import datetime, timedelta
from PIL import Image

# 画像の読み込み
image = Image.open('omochabako.png')
# 画像を表示
st.image(image, caption='Image caption', use_column_width=True)

 #cssファイルの内容を読み込み
with open("style.css") as f:
    css = f.read()
 #css適用
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# サイドバーに表示
name1 = st.text_input("整理(せいり)する人（ひと）の名前（なまえ）")
name = st.sidebar.text_input("整理(せいり)したいものを入力してね")
date = st.sidebar.date_input("整理（せいり）する日付（ひづけ）を入力してね")

# タイトル表示
st.markdown("<h1 style='text-align: center;'>☆ときめき断捨離（だんしゃり）☆アプリ</h1>", unsafe_allow_html=True)

# ページ選択用のサイドバー
page = st.sidebar.selectbox("ページを選択してください", ["こども", "おとな"])
# こども、おとなのページごとのコンポーネント表示
#第1画面
if page == "こども":
  st.markdown("<h1 style='text-align: center;'>☆ときめきはあるかな？☆</h1>", unsafe_allow_html=True)
  st.write("こども用") 
  st.image("images.jfif",caption =f" ↓↓↓{name1}は{date}に{name}にときめくかな？↓↓↓", use_column_width=True)
  st.markdown("<h1>あそんでいないおもちゃたちがいるよ！どうする？</h1>", unsafe_allow_html=True)
  st.markdown("<h1 style='text-align: center;color: white;font-size: 20px;'>☆これからおもちゃたちをどうするかきめよう☆</h1>", unsafe_allow_html=True)

#第2画面  
elif page == "おとな":
    st.markdown("<h1 style='text-align: center;'>♡ときめきはあるかな？♡</h1>", unsafe_allow_html=True)
    st.write("おとな用")
    st.image("images (1).jfif",caption =f" ↓↓↓{name1}は{date}に{name}にときめきますか？↓↓↓", use_column_width=True)
    st.markdown("<h1>使っていないもの！これから使う予定はあるの？</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;color: white;font-size: 20px;'>☆断捨離をしてお部屋をすっきりさせよう☆</h1>", unsafe_allow_html=True)
   
st.markdown(f"<h1 style='text-align: center; color: pink;'>{name}</h1>", unsafe_allow_html=True)

 # こどものチェック
if page == "こども":
  #ラジオボタンのYES/NO使用。文書き換え(こども用)
  q1 = st.radio('1.あたらしいもの？', ['そうだよ','ちがうよ'])
  q2 = st.radio('2.いまあそんでいるもの？', ['そうだよ','ちがうよ'])
  q3 = st.radio('3.それはこわれていない？', ['そうだよ','ちがうよ'])
  q4 = st.radio('4.それはなにかにつかえる？', ['そうだよ','ちがうよ'])
  q5 = st.radio('5.それはあしたもあそぶの？', ['そうだよ','ちがうよ'])
 # おとなのチェック
else:
  #ラジオボタンのYES/NO使用。文書き換え(おとな用)
  q1 = st.radio('1.最近買いましたか？', ['はい','いいえ'])
  q2 = st.radio('2.それは最近使いましたか？', ['はい','いいえ'])
  q3 = st.radio('3.それは壊れていませんか？', ['はい','いいえ'])
  q4 = st.radio('4.それは再利用できますか？', ['はい','いいえ'])
  q5 = st.radio('5.それは明日も使いますか？', ['はい','いいえ']) 

st.markdown("<h1 style='color: blue;'></h1>", unsafe_allow_html=True)

#そうだよ、はいのカウント数を加算
#変数の(count)は、「そうだよ」または「はい」と答えた質問の数をカウントするために使う。
#or演算子を使っているため、いずれかの条件が真であればcountを1増やす。
#ﾘｽﾄとﾙｰﾌﾟを使う
#変数（count）を0で初期化。
count = 0
questions = [q1, q2, q3, q4, q5]
for q in questions:
    if q == "そうだよ" or q == "はい":
        count += 1 
if count == 5:
 # text_input=("すてない")
  st.markdown("<h1 style='text-align: center;'>すてない！</h1>", unsafe_allow_html=True)
  st.markdown("<h1 style='text-align: center;color: pink;font-size: 30px;'>たいせつにしようね</h1>", unsafe_allow_html=True)
elif count>=4: 
 # text_input= ("3日考える")
  st.markdown("<h1 style='text-align: center;'>3日（みっか）かんがえるよ！</h1>", unsafe_allow_html=True) 
  st.markdown("<h1 style='text-align: center;color: pink;font-size: 20px;'>3日（みっか）かんがえるよ!の場合（ばあい）は左画面（ひだりがめん）3日後（みっかご）ボタンをおしてね</h1>", unsafe_allow_html=True)
elif count >=3:
 #  text_input= ("1日考える")
  st.markdown("<h1 style='text-align: center;'>1日（いちにち）かんがえるよ！</h1>", unsafe_allow_html=True)
  st.markdown("<h1 style='text-align: center;color: pink;font-size: 20px;'>1日（いちにち）かんがえるよ!の場合（ばあい）は左画面（ひだりがめん）1日後（いちにちご）ボタンをおしてね</h1>", unsafe_allow_html=True)
else:
 #  text_input= ("すてる")
 st.markdown("<h1 style='text-align: center;'>すてるよ！</h1>", unsafe_allow_html=True)
 st.markdown("<h1 style='text-align: center;color: pink;font-size: 20px;'>すてるよ!の場合（ばあい）は左画面（ひだりがめん）メルカリHPやリレーションセンターHPを参考（さんこう）にしてね</h1>", unsafe_allow_html=True)
st.sidebar.markdown("[メルカリ公式サイト](https://jp.mercari.com/)")
st.sidebar.markdown("[生駒市清掃リレーセンター](https://www.city.ikoma.lg.jp/0000001349.html)")

if page == "こども":
  st.markdown(f"<h1 style='text-align: center; color: white;font-size: 30px;'> ☆そうだよのかずでどうするかきまるよ☆</h1>", unsafe_allow_html=True)
else:
  st.markdown(f"<h1 style='text-align: center; color: white;font-size: 30px;'>　☆はいの数でどうするかきまるよ☆</h1>", unsafe_allow_html=True)
  
st.markdown(f"<h1 style='text-align: center; color: white;font-size: 30px;'>{count}</h1>", unsafe_allow_html=True)

di = {
    "そうだよ,はいの数（かず）５の場合（ばあい）": "捨（す）てない",
   "そうだよ,はいの数（かず）４の場合（ばあい）": "３日（みっか）考（かんが）える。３日後（みっかご）のボタンを押（お）してね",
    "そうだよ,はいの数（かず）３の場合（ばあい）": "１日（いちにち）考（かんが)える。1日後（いちにちご）のボタンを押(お)してね",
    "そうだよ,はいの数（かず）２，１の場合（ばあい）": "捨（す）てる",
}

st.write("##対応表##")
for key, value in di.items():
    st.write(f"- **{key}**: {value}")
    

# 現在の日付を取得
today = datetime.today().date()

# コメントの入力日とボタンの状態を保存するための変数
if 'comment_date' not in st.session_state:
    st.session_state['comment_date'] = None
if 'button_pressed' not in st.session_state:
    st.session_state['button_pressed'] = None

# 3日後のボタンが押された場合の処理
if st.sidebar.button("３日後ボタン"):
    st.session_state['comment_date'] = today
    st.session_state['button_pressed'] = '3_days'
    st.write("３日かんがえてね")

# 1日後のボタンが押された場合の処理
if st.sidebar.button("１日後ボタン"):
    st.session_state['comment_date'] = today
    st.session_state['button_pressed'] = '1_day'
    st.write("１日かんがえてね")

# コメントの表示処理
if st.session_state['comment_date']:
    if st.session_state['button_pressed'] == '3_days':
        comment_display_date = st.session_state['comment_date'] + timedelta(days=3)
        if today >= comment_display_date:
            st.write("ときめきますか")
        else:
            st.write(f"コメント表示まであと{(comment_display_date - today).days}日です。")
    elif st.session_state['button_pressed'] == '1_day':
        comment_display_date = st.session_state['comment_date'] + timedelta(days=1)
        if today >= comment_display_date:
            st.write("ときめきますか")
        else:
            st.write(f"コメント表示まであと{(comment_display_date - today).days}日です。")

#こども、おとなごとに挿入イラストを変える
options = ["こども","おとな"]
  #こども
if page == "こども":
  child = ("こども")
  is_child = True 
  st.image("kuruma.jfif",caption =f"↓↓↓せいりせいとん↓↓↓", use_column_width=True)
  time.sleep(1)
  st.markdown("<h1>ときめかないものはバイバイしよう</h1>", unsafe_allow_html=True)
else:
  #おとな
  is_adult = True
  st.image("pikapika.jfif",caption =f"↓↓↓(整理整頓)↓↓↓", use_column_width=True)
  time.sleep(1) 
st.markdown("<h1>ときめかないものはすてましょう</h1>", unsafe_allow_html=True)


#以下にテキスト入力
st.markdown(f"<h1 style='text-align: center; color: white;font-size: 30px;'> ☆メモ☆</h1>", unsafe_allow_html=True)
st.text_input("メモ", key="do")
st.session_state.do #keyでアクセス


st.markdown(f"<h1 style='text-align: center; color: white;font-size: 30px;'> ☆今後（こんご）の予定（よてい）☆</h1>", unsafe_allow_html=True)
# Input for the task
task = st.text_input("すること")

# Input for the date
date = st.date_input("作業予定日（さぎょうよていび）")

# Initialize the tasks list in session state if it doesn't exist
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Button to add the task
if st.button("追加（ついか）"):
    if task and date:
        st.session_state.tasks.append({"task": task, "date": date})
        st.success("タスクが追加されました！")

#st.write("### ☆今後の予定")
today = datetime.today().date()
for task_info in st.session_state.tasks:
    task_date = task_info["date"]
    task_desc = task_info["task"]
    if task_date <= today:
        st.write(f"{task_date}: {task_desc} - ")
    else:
        st.write(f"{task_date}: {task_desc}")

if st.button("リセット"):
    st.session_state.tasks = []
    st.success("すべてのタスクがリセットされました！")

   #チェックボックス
st.title("ごみ捨（す）てチェック")
is_agree = st.checkbox("ごみ捨（す）てた？")     


