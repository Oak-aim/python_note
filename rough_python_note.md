```python
-　すばやく効果的にシステムを開発できるように作られた汎用プログラミング言語 

  

-　本格的なWebサービスの開発 

機械学習・AI、理学計算、統計解析 

  

-　Google、YouTube、Instagram、Dropbox 

  

特徴：Script言語で開発がしやすい。 

　　　様々な分野のLibraryがある。 

　　　機械学習・Big　Data分析 

　　　だれがかいても、同じような書き方になる。 

  

Python ネスト：Pythonのネスト（入れ子）は、if文、for/whileループ、関数、データ構造（リストや辞書）などの内部に、同じ種類の構造を階層的に組み込むことです。 

 

用語 

意味 

query 

問い合わせ・検索条件 

SQL query 

データベースへの命令 

pandas query 

データ抽出の条件式 

 

int　➞　整数扱い 

float　➞　浮動小数点 

str　➞　文字列扱い 

 

-------------------------------------------------------------------------------------------------------------------- 

演算子： 

 

算術演算子　➞　+, -, *, /, //, ... 

代入演算子　➞　=, ... 

ブール演算子　➞　and, or, not 

比較演算子　➞　<, ==, >, !=, >=, <=, in, not in 

 

割り算　➞　(-13/4) ➞ -3.25　(-13//4) ➞ -4 

浮動小数点の値をコンピュータが正確に取得できず、誤差がある 

 

べき乗：n の n 乗 

print(5 ** 2)  ➞　25 

 

in/not in 演算子： 

s = "abc" 

print("a" in s)            #   True 

print("d" not in s)     #   True 

 

ブール演算子： 

and： 

a = 1 == 1               #   比較演算子の結果を代入 

b = 1 >= 0 

print(a and b)       #  True 

 

c = 10 < 10 

print(a and b or c)       #   False 

 

or： 

a = 1 < 0 

b = 1 >= 1 

print(a or b)       #  True 

 

c = 1 == 0 

print(a or b or c)       #  True 

 

否定を演算(not)：A が True のとき False になり、False のときは True になる演算 

 

a = 0 == 0 

print(a)                   #  True 

print(not a)            #  False 

  

li = [1, 2, 3] 

print(not 1 in li)  # 非推奨、False 

print(1 not in li)  # 推奨、False 

 

 

ブール演算の優先順位： 

 

a, b, c = 1, 2, 3 

print(not a == 1 and b == 2)                       #False 

print(a == 1 or b == 1 and c == 1)             #Ture 

print(not a == 4 or c == 3)                          #True 

print(not a == 1 and b == 3 or c == 2)                 #False 

print(not(a == 1 and (b == 3 or c == 2)))             #True 

 

 

 

 

-------------------------------------------------------------------------------------------------------------------- 

演算子　優先順位： 

高い ( ) 

｜** * / % 

低い + - 

 

例：name[(M - 1) % N]  

式で割り当てる回数をループして一個当たり出力できる！ 

 

-------------------------------------------------------------------------------------------------------------------- 

コメントを入力する： 

  

# print("......") 

   

''' 

print(".....") 

''' 

 

-------------------------------------------------------------------------------------------------------------------- 

print()関数： 

print(".....") 

print('''hello, my friend, Oak''') 

print("...", "...", "...")         #　空白で出力、複数の文字列の出力 

  

print関数で改行したくない場合： 

print("...", end="")          #　空の文字列、長さ０ 

print("...", end="") 

print("...", end="") 

 

入力された文字列を改行し、出力： 

std_in = input() 

for string in std_in.split(): 

    print(string) 

 

こういう書き方で出力をマージンからインデントあげられる： 

 

print(f"""User{{ 

nickname : {self.name} 

old : {self.age} 

birth : {self.birth} 

state : {self.state} 

}}""") 

 

出力： 

 

User{ 

    nickname : mako 

old : 13 

birth : 08/08 

state : nara 

} 

 

s = "Hello, World!" 

Print(s[0])  # H 
print(s[-1]) # 文字列 s の末尾の文字列が出力される 
print(s[-2])  # 文字列 s の末尾から 2 番目の文字列が出力される 

 

s = "Hello, World!" 

print(s[1:4])  # ell 

print(s[:5])    # Hello 

print(s[7:])    # World! 

 

 

大文字に切り替える： 

c = input() 

print(c.upper()) 

-------------------------------------------------------------------------------------------------------------------- 

len：「文字列の長さ」とは、「文字列の文字数」のこと 

 

s = "Hello, World!" 

print(len(s))       # 13 

 

文字列の結合(+)：2 つの文字列をつなげること 

 

s = "Hello " 

t = "World!" 

print(s + t)     #Hello World! 

print(s, t)       #Hello  World! 

s = s + t 

print(s)          #Hello World! 

 

文字列の反復(*)：同じ文字列を何度も繰り返すこと 

 

s = "abc" 

n = 2 

s *= n 

print(s)      #abcabc 

 

ｆ文字列：f'変数 x が示す値は {x} だ' のように f 文字列を使うと、文字列内の波括弧の箇所が変数 x の値で置換される 

 

time = "10"       # int を str に変換してくれる 

place = "会議室 A" 

print(f"{time}時から{place}で会議がおこなわれる。")　#10時から会議室 Aで会議がおこなわれる。 

 

-------------------------------------------------------------------------------------------------------------------- 

変数　使い方： 

player = "勇者" 

print(player + "は、荒野を歩いていた") 

  

-------------------------------------------------------------------------------------------------------------------- 

int型から string型へ転換： 

number = 100 

print("スライムが" + str(number) + "匹あらわれた") 

  

-------------------------------------------------------------------------------------------------------------------- 

random値： 

import random                           #  ramdom module を組み込む 

number = random.randint(1,100)　        #  1 から 100 

attack = random.randrange(number)       #   

number1 = random.random() 

  

-------------------------------------------------------------------------------------------------------------------- 

関数の処理結果を　戻り値　と呼ぶ 

上記通り、(1,100)引数と指定したら、戻り値として出力する 

  

-------------------------------------------------------------------------------------------------------------------- 

条件分岐： 

ループ脱出：break 文を使うと、while 文のループ処理を脱出することができる 

処理をスキップ：continue 文を使うと、while 文によるループ処理を 1 周スキップできる 

 

if number == 1: 

   print( "スキ！")  

elif number == 2: 

print( "キライ") 

else: 

 

pass 文： 

 

a = -10 

if a < 0: 

    pass          #  pass して何の処理も行わない 

  

-------------------------------------------------------------------------------------------------------------------- 

今の年（2026年）を取得する： 

 

import datetime 

seireki = datetime.date.today().year 

  

-------------------------------------------------------------------------------------------------------------------- 

for inループ記述式とrange関数： 

ループ脱出：break 文を使うと、while 文のループ処理を脱出することができるが、2重ループなら、どちらかをい１つを考える 

処理をスキップ：continue 文を使うと、while 文によるループ処理を 1 周スキップできるが、同上 

 

for i in range(10): 

    print("Hello World") 

  

range(10) 0から9まで、10回繰り返す 

range(6, 11) 6から10まで繰り返す 

  

-------------------------------------------------------------------------------------------------------------------- 

while処理： 

ループ脱出：break 文を使うと、while 文のループ処理を脱出することができるが、2重ループなら、どちらかをい１つを考える 

処理をスキップ：continue 文を使うと、while 文によるループ処理を 1 周スキップできるが、同上 

 

i = 1 

while i <= 10: 

    print(i) 

    i = i + 1 

  

-------------------------------------------------------------------------------------------------------------------- 

入力式： 

 

line = input() 

print("hello " + line) 

  

line = int(input()) 

print(line) 

  

for i in range(count): 

    line = input().rstrip()  #行末の改行を削除すること 

    print("hello " + line) 

  

line = input().rstrip().split(" ") 

  

-------------------------------------------------------------------------------------------------------------------- 

リスト： 

並び順が必要なデータ 

トランプや将模などのゲームデータ 

Web選択フォーム 

エクセルような複数CSVデータ処理（コマ区切ったText Fileようなデータ） 

 

player_1 = "戦士" 

player_2 = "魔法使い" 

team = ["勇者", "魔法使い", 100, player_1] 

print(team) 

出力：['勇者', '魔法使い', 100, '戦士'] 

 

リストの末尾追加： 

team = ["勇者", "魔法使い"] 

team.append("戦士") 

print(len(team)) 

出力：３ 

 

リスト入れ替え： 

team[2] = "ドラゴン" 

print(team) 

出力：['勇者', '魔法使い', 'ドラゴン'] 

 

リスト削除： 

team.pop(2) 

print(team) 

出力：['勇者', '魔法使い']  

 

正のインデックス： 

li = [5, 3, 8] 
print(li[1]) 

 

負のインデックス： 

li = [5, 3, 8] 
print(li[-1])  # リスト li の末尾の要素が出力される 
print(li[-2])  # リスト li の末尾から 2 番目の要素が出力される 

 

リストの取得方法： 

li = ["A", "B", "C", "D", "E"] 

print(li[1:4])         #  ['B', 'C', 'D']、「i ～ j - 1」指定 

print(li[:3])           #  ['A', 'B', 'C']、「どこから」指定 

print(li[2:])           #  ['C', 'D', 'E']、「どこまで」指定 

print(li[:])             #  ['A', 'B', 'C', 'D', 'E']  「すべて」指定 

 

リストの長さ取得： 

len(li) 

 

リスト連結： 

a = [1, 2, 3] 
b = [4, 5, 6] 
print(a + b)          # [1, 2, 3, 4, 5, 6] 

 

リストの反復(*)：同じ要素の繰り返しをもつリストを作る 

li = [1, 2, 3] 

n = 2 

print(li * n)         #  [1, 2, 3, 1, 2, 3] 

 

リストの末尾に要素を追加(append)： 

li.append(4) 

 

リストの末尾の要素を削除しながら取得(pop)： 

li = [1, 2, 3, 4] 

a = li.pop()         #  [1, 2, 3] 

 

リストの要素を指定して削除(remove)：要素が複数ある場合、左から最初に見た要素（要素最小値）が削除される 

li = [1, 2, 3, 4, 3] 

li.remove(3)        #  [1, 2, 4, 3] 

 

リストのインデックス i の要素を削除(del)：要素を指定して削除する、リストの取得方法でも削除できる 

li = [5, 3, 4, 3, 2] 

del li[1]        #  [5, 4, 3, 2] 

 

リストの要素をソート 1 (sort)：並べ替える（デフォルト：昇順）、リストそのものの要素の順番を変えることを破壊的にソートする、混雑リスト [1, 2, 3, "a"] には向いていない 

sort() はリストに対して使うメソッドです 

b = ["apple", "cat", "banana"] 

b.sort()        #  ['apple', 'banana', 'cat'] 

 

a = [1, 3, 2] 

a.sort()        #  [1, 2, 3] 

 

c= [1, 3, 2] 

c.sort(reverse=True)        #  [3, 2, 1] 

 

リストの要素をソート 2 (sorted)： 

a = [1, 3, 2] 

li = ["cat", "apple", "banana"] 

print(sorted(a))        #  [1, 2, 3]、文字列も同様 

a = sorted(li, reverse=True)      #  ['cat', 'banana', 'apple'] 

 

リスト → 文字列変換： join メソッドを使うと、リスト li の各要素を結合することができる 

li = ["A", "B", "C"] 

print(" ".join(li))  # 半角スペースを区切り文字として結合、A B C 

print("".join(li))  # 空文字列を区切り文字として結合、ABC 

print("/".join(li))  # スラッシュ(/) を区切り文字として結合、A/B/C 

 

文字列 → リスト：list()メソッドを使うと、リストの各要素に格納される 

s = "paiza" 

print(list(s))       #  ['p', 'a', 'i', 'z', 'a'] 

 

s = "apple,banana,cat" 

t = "," 

print(s.split(t))       #   ['apple', 'banana', 'cat'] 

print(s.split("a"))        #  ['', 'pple,b', 'n', 'n', ',c', 't'] 

 

リストやタプルのインデックスと要素の組を取得(enumerate)： 

リスト li のインデックスと、そのインデックスに対応する要素の組を取得できる 

リストのインデックスと要素の組だけでなく、タプルなどイテラブル全般のインデックスと要素の組を取得できる 

取得できる値は、(インデックス, 要素) の組を表すタプルを、イテラブルの長さ分もった値 

 

li = ["apple", "banana", "melon"] 

e = enumerate(li) 

for t in e: 

    print(t) 

for i, a in enumerate(li): 

    print(i, a) 

for i, a in enumerate(li, 23): 

    print(i, a) 

 

while と for の使い分け： 

while文： 

繰り返し回数は柔軟に決めたいとき 

毎回条件式によって「繰り返し処理を続けるか」判定を行う） 

1 + 2 + 3 + ... と順に整数を足していったとき、何回目ではじめて 10000 を超えるか、を調べたいときなど 

 

for文： 

繰り返し回数は明確に決まっている時 

break 文などの例外もあるが、for 文は in (イン) のうしろに書かれる値によってあらかじめ繰り返す回数が決められる 

また、リストなどの要素を先頭から順に取得することが簡単にできる 

これらのことから、繰り返す回数が明確に決まっている」ときに for 文は有用 

たとえば、リストのすべての要素を出力したり、range 関数を使って 100 回同じことをしたいときなど 

 

-------------------------------------------------------------------------------------------------------------------- 

HTMLでドロップダウン： 

print("<select name='job'>") 

for job in team: 

    print("<option>" + job + "</option>")  

print("</select>") 

 

読み取ったデータを配列リストに入れ込む： 

line = input().rstrip().split(",") 

print(line) 

 

split(",")：引数で指定したコンマで分割してリストして代入する 

スライム,モンスター,ドラゴン,魔王　➞　要素数「4」 

スライム、モンスター、ドラゴン、魔王　➞　要素数「1」 

 

split("、") 

スライム,モンスター,ドラゴン,魔王　➞　要素数「1」 

スライム、モンスター、ドラゴン、魔王　➞　要素数「4」 

 

入力：https://paiza.jp/cgc/users/ready 

url_str = input().rstrip().split("/") 

print(url_str) 

出力：['https:', '', 'paiza.jp', 'cgc', 'users', 'ready'] 

 

print(people[i]) 

print(people[i + 1]) 

print(len(people)) 

 

-------------------------------------------------------------------------------------------------------------------- 

標準入力： 

入力は何行あっても読み取れる・全行を読み取った後、ループを抜ける・ 

改行もふくめて読み取る！ 

 

import sys 

for line in sys.stdin.readlines():  

print(line.rstrip()) 

 

空のarrayリストの末尾に追加してくれる！ 

array = [] 

for line in sys.stdin.readlines():   

    array.append(line.rstrip()) 

print(array) 

 

hour, minute = map(int, input().split())      #int 入力 

 

複数列の入力値から文字列・整数のリストを生成： 

入力：cat.fly.fish 

a = input().split() 

出力：{cat, fly, fish} 

 

入力：2.1 3.8 5.2 

li = [] 

a = input().split() 

for x in a: 

    li.append(float(x)) 

print(li) 

出力：[2.1, 3.8, 5.2] 

 

複数列の入力値から内包表記でのリストを生成： 

入力：1 12 123 

li = [int(x) for x in input().split()] 
print(li) 

出力：[1, 12, 123] 

 

複数列の入力値を map 関数でそれぞれ整数値に変換： 

 

空白あり２つ目の値入力： 

入力：user_id: python 

 

_, user_id = input().split(" ") 

print(f"hello {user_id} !") 

 

出力：Hello python ! 

 

-------------------------------------------------------------------------------------------------------------------- 

辞書の使い方： 

DBとやりとりするデータ処理！ 

APIとやりとりするデータ処理！ 

辞書とは、2 つの値の組を複数組まとめて管理できる型 

2 つの値は次の通り 

key 

key に対応づけられた value 

辞書と key を指定することで、key と組になっている value を特定できる 

key で value を検索するため、キーを重複させることはできない 

辞書で管理する key と value の組のことを「辞書の要素」という 

辞書で管理できる要素の数は可変で、好きなだけ要素を追加できる 

辞書の key にできる型の例 

文字列 

タプル        #print({(1, 2): "ab", (3, 4): "cd"}) 

整数 

浮動小数点数 

数列 

辞書の key にできない型の例 

リスト        #print({[1, 2]: "ab", [3, 4]: "cd"}) 

辞書 

 

辞書の長さ：「辞書の要素数」のこと 

print(len(dc)) 

 

辞書での要素の追加・更新： 

追加：dc[k] = v 

dc = {"apple": 150, "banana": 150, "melon": 2000} 

dc["orange"] = 130                # {'apple': 150, 'banana': 150, 'melon': 2000, 'orange': 130} 

 

更新：dc[k] = v 

dc = {"apple": 150, "banana": 150, "melon": 2000} 
dc["apple"] = 200                                 # {'apple': 200, 'banana': 150, 'melon': 2000} 

 

要素削除：del dc[k] 

dc = {"apple": 150, "banana": 150, "melon": 2000} 

del dc["apple"]                                 # {'banana': 150, 'melon': 2000} 

 

辞書の keys をすべて取得(key)：dc.keys() 

dc = {"alice": 162, "bob": 178, "carol": 155} 

print(dc.keys())                                 # dict_keys(['alice', 'bob', 'carol']) 

 

for key in dc.keys():/for key in dc: 

    print(key)                                 # alice bob carol 

 

辞書の values をすべて取得：dc.values() 

keys の取得したかと同じ！ 

 

辞書の key と value の組をすべて取得(items)：dc.items() 

dc = {"alice": 162, "bob": 178, "carol": 155} 

for key, value in dc.items(): 

    print(key, value)                                 # alice 162, bob 178, carol 155 

 

for item in dc.items(): 

    print(item)                                 # ('alice', 162), ('bob', 178), ('carol', 155) 

 

辞書の key として含まれるか(in)：s in dc 

 

dc = {"alice": 162, "bob": 178, "carol": 155} 

print("bob" in dc)                                 # True 

print("dave" in dc)                                # False 

 

辞書の key をソート(sorted)：sorted(dc) 

 

dc = {"orange": 130, "banana": 150, "apple": 150, "melon": 2000} 

k = sorted(dc) 

print(sorted(dc))                                # ['apple', 'banana', 'melon', 'orange'] 

 

for key in k: 

    print(key, dc[key])                          # apple 150, banana 150, melon 2000, orange 130 

 

内包表記で辞書を生成： 

 

a = {} 

for i in range(10): 

    a[i] = i * 2 

print(a)              # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18} 

 

b = {x: x*2 for x in range(10)} 

print(b)              # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18} 

 

dc = {K: V for B in C} 

# K: 0 などの明示的な値や変数、または式 ･･･ 辞書 dc の key になる 

# V: 0 などの明示的な値や変数、または式 ･･･ K で指定する key に対応する value になる 

# X: 変数 ･･･ C の各要素を受ける 

# Y: イテラブル (リストやタプルなど) 

 

書き方： key : value 

 

enemyDictionary = { "ザコ":"スライム", "中ボス":"ドラゴン" } 

 

しかし、出力するときはバラバラなのでKey（キー）を指定して出力できる： 

print(enemyDictionary["ザコ"]) 

 

変数で指定して、出力できる： 

 

level = "ザコ" 

print(enemyDictionary[level]) 

 

あいうえお順： 

漢字・カタカナの時、整列にならん 

 

weapons = ["knife", "gun"] 

print(sorted(weapons)) 

             OR 

weapons2 = ["2.knife", "1.gun"] 

print(sorted(weapons2)) 

 

sorted_skills = dict(sorted(skills.items())) 

print(sorted_skills) 

 

おいうえお逆順： 

 

print(sorted(weapons, reverse=True)) 

 

Common dictionary methods 

.keys() → returns all keys 

.values() → returns all values 

.items() → returns key–value pairs 

.update() → updates dictionary 

 

students = { 

    "student1": {"name": "Alice", "age": 21}, 

    "student2": {"name": "Bob", "age": 22} 

} 

student = { 

    "name": "Alice", 

    "age": 21, 

    "course": "Computer Science" 

} 

print(student["name"])      # Alice 

print(student.get("age"))  # 21 

 

student["age"] = 22          # update 

student["grade"] = "A"       # add new key 

 

student.pop("age")           # removes 'age' 

del student["grade"]         # deletes 'grade', can delete Objective 

 

for key, value in student.items(): 

    print(key, value) 

 

for key in student: 

    print(student[key]) 

            OR 

for range in skills: 

    print(skills[range]) 

 

足し算したいなら、values() を記述する: 

 

points = {"国語" : 70, "算数" : 35, "英語" : 52} 

for value in points.values(): 

    sum += value 

print(sum) 

 

-------------------------------------------------------------------------------------------------------------------- 

Tuple（タプル）：データ構造の一種、内容更新不可 

タプルは複数の値をまとめて静的に管理する型である 

 

t = (2, 4, 6) 

t[0] = 0                # エラーが発生する 

 

Tuple生成：どのような型の値でも混雑しても、タプルの要素にすることができる 

 

t = 1, 2, 3 

t = (1, 2, 3) 
print(t)              #  (1, 2, 3) 

 

a = (1, 5, 2)  # 要素が整数値のみのタプルを生成 

b = ("apple", "banana", "cat")  # 要素が文字列のみのタプルを生成 

c = ([0, 3, 6], [1, 4, 7], [2, 5, 8])  # 要素がリストのみのタプルを生成 

d = (a, b, c)  # 要素がタプルのみのタプルを生成 

e = (99, "drive", [97, 100, 103], d) 

  

print(a) 

print(b) 

print(c) 

print(d) 

print(e) 

 

出力： 

(1, 5, 2) 

('apple', 'banana', 'cat') 

([0, 3, 6], [1, 4, 7], [2, 5, 8]) 

((1, 5, 2), ('apple', 'banana', 'cat'), ([0, 3, 6], [1, 4, 7], [2, 5, 8])) 

(99, 'drive', [97, 100, 103], ((1, 5, 2), ('apple', 'banana', 'cat'), ([0, 3, 6], [1, 4, 7], [2, 5, 8]))) 

 

print(sorted(weapons.items()))              #items() はキーと値が１組ペアになる・Truple 

 

出力： 

[("gun", 99), ("fireball", 34), ("waterpowder", 12)] 

 

数字を昇順で： 

 

x[0] → 名前（キー）でソート 

x[1] → 点数（値）でソート  

 

print(sorted(weapons.items(), key=lambda x: x[0])) 

                      OR 

print(sorted(weapons)) 

 

print(sorted(weapons.items(), key=lambda x: x[1])) 

        OR 

def get_value(x): 

    return x[1] 

 

出力： 

("waterpowder", 12) ("gun", 99) ("fireball", 40) 

 

#######EXAMPLE####### 

items_imges = { 

    "剣" : "http://paiza.jp/learning/images/sword.png", 

    "盾" : "http://paiza.jp/learning/images/shield.png", 

    "回復薬" : "http://paiza.jp/learning/images/potion.png", 

    "クリスタル" : "http://paiza.jp/learning/images/crystal.png" 

} 

 

cnt = int(input()) 

items_orders = [] 

  

for _ in range(cnt):     #「回数だけ必要で、中身はいらない」という意味、この変数は使いません 

    items = input() 

    items_orders.append(items) 

     

for items in items_orders: 

    print(f"<img src='{items_imges[items]}'>") 

 

タプルをアンパック：Tupleのすべて要素を取り出してそれぞれを一気に変数に代入 

タプルをアンパックした後、その Tuple の要素はそのまま消えない 

タプルのインデックス i の要素をリストみたい取得できる 

タプルのインデックスが i ~ j-1 の要素をリストみたい取得できる 

タプルの長さを取得(len) 

タプルの結合（＋） 

タプルの反復(*) 

 

a, b, c = (1, 2, 3) 

print(a, b, c) 

print(a)        # 1 

 

t = (2, 4, 6, "apple", "cat") 

print(len(t))          #  5 

 

a = (2, 4, 6) 
b = ("apple", "banana", "cat") 
print(a + b)       # (2, 4, 6, 'apple', 'banana', 'cat')、新しタプルけど、元の要素数は変わらん 

 

t = (1, 2, 3) 

n = 2 

print(t * n)                    #  (1, 2, 3, 1, 2, 3) 

 

Tupleのまとめ：複数の値を静的に管理できるところ 

たとえば、異なる型の値をタプルの要素にしても、不具合やバグの心配がない 
リストは、複数の値に対してさまざまな操作をしながら、動的に管理していくことが念頭におかれた型であるため、異なる型の値があると、不具合やバグの原因になることがある 

また、タプルを適切に使うことで、わかりやすいコードを書くことができる 

 

 

-------------------------------------------------------------------------------------------------------------------- 

2次元リスト： 

 

 

配列の末尾追加： 

 

teams = [ 

["A", "B"],  

["C", "D", "E"] 

] 

teams.append(["E", "G"]) 

print(teams) 

 

teams[0].append("1") 

print(teams) 

 

del teams[1] 

print(teams) 

 

出力：["A", "B"], ["C", "D", "E"], ["E", "G"] 

["A", "B", "1"] 

["A", "B"],  ["E", "G"] 

 

enumerate：「インデックス（番号）付きでループできる」関数 

 

team = ["勇者", "戦士", "魔法使い"] 

for (i, person) in enumerate(team): 

    print(str(i + 1) + "番目の" + person + "が、スライムと戦った") 

 

リストの初期化： 

 

numbers = [1 for i in range(10)] 

print(numbers) 

 

numbers = [i * 2 for i in range(10)] 

print(numbers) 

 

numbers2 = [[1 for i in range(3)] for j in range(4)] 

print(numbers2) 

 

出力：[1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18] 

[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]] 

 

-------------------------------------------------------------------------------------------------------------------- 

ルース行：左行番後を２で割って余りが０となるところで 

 

 

landmap = [["森" for i in range(20)] for j in range(10)] 

landmap[0][0] = "城" 

landmap[0][19] = "町" 

landmap[9][19] = "町" 

for i,line in enumerate(landmap):           ## 地図の各行を取り出す 

    print(str(i) + ":", end="") 

    for j, area in enumerate(line):　　　　　　             ## 行からエリアを取り出す 

       if (i % 2 == 0 or j % 3 == 0) and area == "森":          ##ルース行 

            print("＋", end="") 

        else: 

            print(area, end="") 

    print()                                                       ## 取り出したデータを改行なしで出力する  

 

-------------------------------------------------------------------------------------------------------------------- 

出力： 

入力： 

1,1,1,1,1 

2,3,3,3,2 

2,4,4,4,2 

_ 

 

ソースコード： 

players_img = [ 

    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Empty.png", 

    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Dragon.png", 

    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Crystal.png", 

    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Hero.png", 

    "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Heroine.png"] 

  

配置データを読み込み： 

 

team = [] 

while True: 

    line = input() 

    if line == "_": 

        break 

    team.append(line.split(",")) 

  

ここから先を入力してください 

print("<table>") 

for line in team: 

    print("<tr>") 

    for player in line: 

        print("<td><img src='" + players_img[int(player)] + "'> </td>") 

        # print("<td>" + player + "</td>") 

    print("</tr>") 

print("</table>") 

 

-------------------------------------------------------------------------------------------------------------------- 

関数の一言：見通しが良くなる・再利用できる 

長いコードを分割して整理 

コードに名前つけられる 

何度も呼び出せる 

コードを組み合わせる 

 

関数の用語： 

仮引数: 関数に渡される値が代入される変数 

引数: 関数に渡される値 

関数を呼び出す: 関数を使う 

返り値: 関数内の処理が終わったときに、「関数の呼び出し元」に返される値 

 

処理を記述する行はインデントを 1 つ多くする 

インデントは半角スペース 4 つが推奨されている 

処理のまとまりごとにインデントを揃える 

 

def：関数定義 

1文字目　→　アルファベット・アンダバー 

2文字目以降　→　アルファード・アンダバー・数字 

❌大文字❌ 

 

def say_hello(): 

print("Hello!")  

 

関数の中から関数を呼び出す： 

 

def twice(x): 

    return x * 2 

def increment(x): 

    return x + 1 

def twice_and_increment(x): 

    return increment(twice(x)) 

print(twice_and_increment(3))                 #   7 

 

関数を呼び出し場所：関数を定義する前に、関数をprint()で呼び出そうとしているため、エラーが発生する 

しかし、定義した関数はprint()の上増のどこにあってもよい 

 

内部関数を定義：関数の内部に定義する関数 

関数内で何度もおこなう処理を内部関数にまとめる 

また、関数のなかからしか呼び出すことができない特性を生かして、 

「関数としてまとめたいが、自由に使われては困る処理」 

「関数としてまとめたいが、関数の外から使うことはなく、自由に使えるようにしても無駄になる処理」といった処理を関数としてまとめることができる 

 

def eight_times(x): 

    def twice(y): 

        return y * 2 

    return twice(x) * 4 

print(eight_times(3))                 #   24 

 

eight_times 関数のなかで定義されている twice 関数が内部関数 

 

return値を書かない場合： 

返り値を書かなかったときは、None が返される 

None とは、NoneType 型の値 

NoneType 型は「なにもない」ことを表す型 

return 文で、返り値を指定しなかったとき 

 

def say_hello(): 

    print("hello") 

    return 

print(say_hello())                 #   hello    None 

 

関数を強制的に終了： 

return 文を書くと、その return 文が実行された時点で関数の処理が終了する 

even_or_odd 関数では、変数 n の示す値が偶数のとき、"偶数" と出力され、関数処理が終了する("奇数" とは出力されない) 

 

def even_or_odd(n): 

    if n % 2 == 0: 

        print("偶数") 

        return 

    print("奇数") 

even_or_odd(4)                 #   偶数 

 

スコープ：変数の有効範囲 

ローカル変数：関数の中の変数（スコープ外の代入・変更❌）　／　 

グローバル変数：関数の外の変数（関数中にも共通）、関数の中からは参照を許可されて、代入や変更は❌ 

どうしても変更を加えたいなら、global　変数… 

 

ローカル変数： 

 

def say_hello(): 

    msg = "hello" 

    print(msg) 

say_hello()                  #   hello 

 

def say_hello(): 

    msg = "hello" 

    print(msg) 

print(msg)                 #   エラー 

  

このコードを実行すると、9 行目でエラーが発生する 

9 行目から使うことのできる変数 msg がないから 

 

グローバル変数として用意したのに、再代入使えない例： 

関数の中で再代入される値は、ローカル関数のみ行われるから 

グローバル変数 x は再代入されたから、エラーが発生する 

関数内ですでにその変数があるかどうか確認が大事！ 

 

x = 1 

def func0(): 

    x *= 2 

    print(f"x = {x}") 

func0()                 #   エラー 

 

しかし、非ローカル変数について処理 (nonlocal：非ロカール変数を利用し、関数同士内で利用する)もある 

 

x = 1 

def func0(): 

    y = x * 2 

    def func1(): 

        nonlocal y 

        y *= 2 

    print(f"y = {y}") 

    func1() 

    print(f"y = {y}") 

func0()                 #   2 4 

 

 

グローバル変数：グローバル変数とは、どこからでも変数の示す値を取得できる変数のこと 

ローカル変数を用意するとき、その変数名は他の関数のローカル変数や、グローバル変数の名前に縛られず自由に決めることができる 

つまり、ローカル変数を用意するとき、どこか他の関数のローカル変数と同じ変数名を使ったり、グローバル変数と同じ変数名を使ったりしても、それぞれは別々の変数として処理される 

例：１➞ 

 

message = "paiza" 

a = 10 

b = 20 

  

def sum(x, y): 

    a = 3 

    global message 

    message += "paiza" 

    print(message + " " + str(a))                 #   paizapaiza 3 

    return x + y 

  

num = sum(a, b) 

print(num)                 #   30 

print(message + " " + str(a))                 #   paizapaiza 10 

 

例：２➞ 

 

x = 1 

def func0(): 

    x = 2 

    def func1(): 

        x = 3 

        print(x) 

    func1() 

    print(x) 

func0() 

print(x)                 #   3 2 1 

 

非ローカル関数：内部関数からみたとき、外側の関数のローカル変数のことを「非ローカル変数」という 

つまり次のコードで、say 関数からみた、say_hello 関数で用意されている変数 msg を非ローカル変数という 

 

def say_hello(): 

    msg = "hello" 

    def say(): 

        pass 

say_hello()                 #   空出力 

 

-- 

 

内部関数からは、非ローカル変数の示す値を取得することができる 

つまり、次のコードの 5 行目ではエラーにならない 

  

def say_hello(): 

    msg = "hello" 

    def say(): 

        print(msg) 

say_hello()                 #   空出力 

 

-- 

func2 関数のなかから、func1 関数のローカル変数を使うことはできず、結果として、func2 関数のなかから使うことのできる変数 x はないため、エラーになる 

変数のスコープを考えるときに大切なことは、インデントの深さではなく、どの関数のなかにあるかといった包含関係 

 

def func0(): 

    def func1(): 

        x = 1 

        return 

    def func2(): 

        return x 

    return func2() 

print(func0())                 #   エラー 

 

グローバル変数として解釈：global 変数を定義し、代入すること、global 文を用いて関数の外側の変数の値を変更 

 

x= 10 

def assign_global_x(): 

    global x 

    x = 2 

  

assign_global_x() 

print(x)                 #   2 

 

-------------------------------------------------------------------------------------------------------------------- 

引数のデフォルト値：引数を初期値（村人）として渡し、introduce()で出力 

⚠️関数（デフォルト値なし引数、デフォルト値設定した引数）：⚠️ 

 

def introduce(name = "村人"): 

    print("私は" + name + "です。") 

  

introduce("勇者") 

introduce() 

 

出力： 

私は勇者です。 

私は村人です。 

 

可変長引数：name　を　*names　にし、配列として使う！ 

 

def introduce(greeting, *names): 

    for name in names: 

        print("私は" + name + "です。" + greeting) 

  

introduce("こんにちは", "勇者", "村人", "兵士") 

 

出力： 

私は勇者です。 

私は村人です。 

私は兵士です。 

 

可変長引数　ー　辞書：**peopleの書き方、キーと値を出力する 

⚠️なお、辞書の中身は引数として値は順調になるとは限らない⚠️ 

 

def introduce(**people): 

    for name, greeting in people.items(): 

        print("私は" + name + "です。" + greeting) 

    print(people) 

  

introduce(hero = "はじめまして", villager = "こんにちは", soldier = "よろしくお願いします") 

 

出力： 

私はheroです。はじめまして 

私はvillagerです。こんにちは 

私はsoldierです。よろしくお願いします 

{'hero': 'はじめまして', 'villager': 'こんにちは', 'soldier': 'よろしくお願いします'} 

 

-------------------------------------------------------------------------------------------------------------------- 

キーワード引数：省略すること・引数代入 

 

def say_hello(greeting = "hello", target = "world"): 

    print(greeting + " " + target) 

  

say_hello("good morning!") 

say_hello(greeting = "ネコ先生", target = "皆さん") 

say_hello(target = "ネコ先生", greeting = "おはようございます") 

say_hello(target = "ネコ先生") 

say_hello(greeting = "おはようございます") 

 

出力： 

good morning! world 

ネコ先生 皆さん 

おはようございます ネコ先生 

hello ネコ先生 

おはようございます world 

 

-------------------------------------------------------------------------------------------------------------------- 

クラス：大規模、WebアプリFrameworkに重要！ 

クラス変数を宣言したクラスのインスタンス全てで共有して利用できる変数。 

 

オブジェクト思考：変数と関数をセットしたもの 

クラスから作成したオブジェクトのことをインスタンスと呼ぶ 

 

インスタンス変数：インスタンスが持つ変数です。 
インスタンス変数は、インスタンスがある限りデータが保持されます。 

 

 

 

class Greeting: 

    def say_hello(self): 

        print("hello python") 

  

paiza = Greeting() 

paiza.say_hello() 

 

コンストラクタ：クラスからオブジェクト作成するときに最初に自動に呼ばれるメソッド 

 

class Player: 

    def __init__(self, job): #コンストラクタ 

        self.job = job #コンストラクタ変数 

         

    def walk(self): 

        print(self.job + "は荒野歩いていた") 

     

player1 = Player("戦士") 

player1.walk() 

  

player2 = Player("魔法使い") 

player2.walk() 

 

-------------------------------------------------------------------------------------------------------------------- 

文字列とリストのメソッド：以下の関数がある 

 

text = "pYthon" 

  

print(text) 

print(text.capitalize()) 

print(text.upper()) 

  

players = "勇者,戦士,魔法使い,忍者" 

list = players.split(",") 

print(list) 

  

list.remove("忍者") 

print(list) 

  

list.append("霧島") 

print(list) 

 

print(msg.islower())  #文字列中の文字全てが小文字 

 

team = ["勇者", "戦士", "魔法使い", "忍者"] 

insert(3, "盗賊") 

 

出力： 

pYthon 

Python 

PYTHON 

['勇者', '戦士', '魔法使い', '忍者'] 

['勇者', '戦士', '魔法使い'] 

['勇者', '戦士', '魔法使い', '霧島'] 

False 

['勇者', '戦士', '魔法使い', '盗賊', '忍者'] 

 

------------------------------------------------------------------------------------------------------------------- 

アクセス制限：メソッドや変数に対する、外部からのアクセスを制限する方法 

クラス中でしか呼べないメソッド（プライベートメソッド） 

 

（ ＿＿method ）→プライベートメソッド 

（ ＿＿variable）→プライベート変数・プライベートプロパティ 

 

------------------------------------------------------------------------------------------------------------------- 

内包表記： 

内包表記とは、リストなどを生成するときの書き方 

内包表記を使うと、リストの角括弧のなかなどに for を埋め込んで要素を指定することができる 

たとえば、内包表記を使うと、0 から 99 までの整数を要素にもつリストを簡潔に生成することができる 

 

ルール： 

li = [A for B in C] 
A：値　➞　リストの要素になる 

B：変数　➞　Cの各要素を受ける 

C：イテラブル（リスト、タプル） 

 
内包表記を使わない例: 

 
li = [0] * 100 
for i in range(100): 
    li[i] = i 
 
内包表記を使う例: 

 
li = [i for i in range(100)] 

 

演算が用いられた内包表記： 

 

------------------------------------------------------------------------------------------------------------------- 

複数列の入力値を map 関数でそれぞれ整数値に変換： 

指定した関数をイテラブルの各要素に使ったときに得られる値を要素にもつ map 型の値を取得できる 

a = map(int, ["1", "2", "3"]) 

print(a)                                         #  <map object at 0x4f8cb6ca1540> 

 

map 関数 + list 関数 

map 関数を使ったときに得られる map 型の値に list 関数を使うと、リスト型に変換した値を取得できる 

a = list(map(int, ["1", "2", "3"])) 
print(a)                                         #  [1, 2, 3] 

 

1 2 3 のような入力値を整数値のリストとして扱うことができる 

 

a = list(map(int, input().split())) 
print(a)                                         # 1 12 123 ➞ [1, 12, 123] 

 

input().split(): 入力値を空白文字で区切ってリストを生成する 

map(int, ...): 1. で生成されたリストの各要素に int 関数を使ったときに得られる整数値を要素にもつ map 型の値を生成する 

list(...): 2. で生成された map 型の値をリストに変換したときの値を生成する 

 

 

map 関数 + アンパック 

map 型の値はイテラブルなため、アンパックすることができる 

 

a, b, c = map(int, ["1", "2", "3"]) 
print(a, b, c)                                         #  1 2 3 

 

1 2 3 のように 3 つの数値が半角スペース区切りで入力されるとわかっているとき、次のコードのように書くことで、それぞれの値を整数値に変換して変数に代入できる 

 

a, b, c = map(int, input().split()) 
print(a, b, c)                                         #   1 12 123 ➞ 1 12 123 

 

input().split(): 入力値を空白文字で区切ってリストを生成する 

map(int, ...): 1. で生成されたリストの各要素に int 関数を使ったときに得られる整数値を要素にもつ map 型の値を生成する 

a, b, c = : 2. で生成された map 型の値を各変数にアンパックする 

 

複数行の入力値から、整数のリストを生成： 

入力：3  

1 

12 

123 

 

n = int(input()) 

li = [0] * n               #li = [int(input() for _ in range(n)] 

for i in range(n):       

    li[i] = int(input()) 

print(li) 

 

出力：[1, 12, 123] 

 

 

入力：3 

1 2 3 4 

5 6 7 8 

9 10 11 12 

 

n = int(input()) 

li = [0] * n 

for i in range(n): 

    a = [] 

    for x in input().split(): 

        a.append(int(x)) 

        li[i] = a      

print(li) 

 

出力：[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 

 

 

 

「文法上必要だが、使わない」変数の名前 

決まり事ではなく慣習 

アンダーバーは「使わない」ことを意味するため、_ = 1 のように代入して使うことなどは推奨されていない 

 

複数行、複数列の入力値を内包表記で受け取る： 

 

入力：3 

1 2 3 4 

5 6 7 8 

9 10 11 12 

 

n = int(input()) 

li = [[int(x) for x in input().split()] for _ in range(n)] 

print(li) 

 

出力：[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 

 

------------------------------------------------------------------------------------------------------------------ 

 

集合： 

Python の集合とは、複数の値をまとめて重複なく管理できる型のこと 

数学の集合を表現したもの 

集合で管理する値のことを「集合の要素」という 

集合で管理できる要素の数は可変で、好きなだけ要素を追加できる 

 

集合の生成： 

 

st = {1, 2, 3} 

print(st)　　　　　　　　　　　　　#     {1, 2, 3} 

 

print({1, 2, 2, 3, 1})　　　　　  #     {1, 2, 3} 

print(set())　　　　　　　　　　　#     空の値 

 

集合の要素にできる型： 

集合の要素にできる型の例 

文字列 

タプル 

整数 

浮動小数点数 

数列 

 

集合の要素にできない型の例 

リスト 

辞書 

集合 

 

 

集合の長さを取得（len）：「集合の要素数」のこと 

 

st = {1, 2, 3} 

print(len(st))　　　　　　　　　　　#  3 

 

st.add(4)　　　　　　　　　　　#  {1, 2, 3, 4} 

st.remove(2)　　　　　　　　　#  {1, 3, 4} 

 

print(1 in st)　　　　#  True 

print(5 in st)　　　　#  False 

 

集合の和、集合の積、集合の差、集合の対称差 

 

集合の和（｜）： 

 

a = {1, 2, 3} 

b = {2, 3, 4, 5} 

print(a | b)　　　　　　　　　#  {1, 2, 3, 4, 5} 

 

b |= a 

print(a)　　　　　　　　　#  {1, 2, 3} 

print(b)　　　　　　　　　#  {1, 2, 3, 4, 5} 

 

a|= b 

print(a)　　　　　　　　　#  {1, 2, 3, 4, 5} 

print(b)　　　　　　　　　#  {2, 3, 4, 5} 

 

集合の積（＆）： 

 

a = {1, 2, 3} 

b = {2, 3, 4, 5} 

print(a & b)　　　　　　　　　#  {2, 3} 

  

a &= b 

print(a)　　　　　　　　    　#  {2, 3} 

print(b)　　　　　　　    　　#  {2, 3, 4, 5} 

 

集合の差（-）：「集合の差」とは片方の集合から、もう片方の集合の要素を除いたときにできる集合のこと 

たとえば、集合 A {1, 2, 3}と集合 B {2, 3, 4, 5} の差は、集合 {1} 

 

a = {1, 2, 3} 

b = {2, 3, 4, 5} 

print(a - b)　　　　　　　　    　#  {1} 

 

a -= b 

print(a)　　　　　　　　    　#  {1} 

print(b)　　　　　　　　    　#  {2, 3, 4, 5} 

 

集合の対称差（^）：「集合の対称差」とは 2 つの集合のどちらか片方のみに属している要素を集めたときにできる集合のこと 

たとえば、集合 A {1, 2, 3}と集合 B {2, 3, 4, 5} の対称差は、集合 {1, 4, 5} 

 

a = {1, 2, 3} 

b = {2, 3, 4, 5} 

print(a ^ b)　　　　　　　　    　#  {1, 4, 5} 

  

a ^= b 

print(a)　　　　　　　　    　#  {1, 4, 5} 

print(b)　　　　　　　　    　#  {2, 3, 4, 5} 

 

集合の一致（==）か（!=）：集合 A と集合 B が完全に重なる、つまり、集合 A, B の要素が完全に同じであることをいう 

 

a = {1, 2, 3} 

b = {3, 2, 1} 

c = {1, 3, 5} 

  

print(a == b)　　　　　　　　    　#  True 

print(a == c)　　　　　　　　    　#  False 

 

集合の属性（<=）：集合 A が完全に集合 B のなかに入るときのことをいう 

つまり、集合 A のすべての要素が集合 B にも属していることをいう  

たとえば、集合 A {1, 3} は集合 B {1, 3, 5, 7} に含まれる 

 

a = {1, 3} 

b = {1, 3, 5, 7} 

c = {0, 1, 2} 

  

print(a <= b)　　　　　　　　    　#  True 

print(a <= c)　　　　　　　　    　#  False 

  

a = {1, 3} 

b = {1, 3, 5, 7} 

c = {0, 1, 2} 

d = {3, 1} 

  

print(a < b)　　　　　　　　    　#  True 

print(a < c)　　　　　　　　    　#  False 

print(a < d)　　　　　　　　    　#  False 

print(d < a)　　　　　　　　    　#  False 

 

集合の属性（>=）：集合 A が完全に集合 B を覆うときのことをいう 

つまり、集合 B のすべての要素が集合 A にも属していることをいう 

たとえば、集合 A {2, 4, 6, 8} は集合 B {2, 6} を含む 

 

a = {2, 4, 6, 8} 

b = {2, 6} 

c = {0, 1, 2} 

  

print(a >= b)　　　　　　　　    　#  True 

print(a >= c)　　　　　　　　    　#  False 

  

d = {6, 8, 2, 4} 

  

print(a >= d)　　　　　　　　    　#  True 

print(d >= a)　　　　　　　　    　#  True 

  

a = {2, 4, 6, 8} 

b = {2, 6} 

c = {0, 1, 2} 

d = {6, 8, 2, 4} 

  

print(a > b)　　　　　　　　    　#  True 

print(a > c)　　　　　　　　    　#  False 

print(a > d)　　　　　　　　    　#  False 

print(d > a)　　　　　　　　    　#  False 

 

内包表記で集合を生成： 

 

st = {A for B in C} 

# A: 0 などの明示的な値や変数、または式 ･･･ 集合 st の要素になる 

# B: 変数 ･･･ C の各要素を受ける 

# C: イテラブル (リストやタプルなど) 

a = set() 

for i in range(10): 

    a.add(i) 

print(a)　　　　　　　　    　#  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 

 

b = {x for x in range(10)} 

print(b)　　　　　　　　    　#  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 

 

------------------------------------------------------------------------------------------------------------------- 

 

replace():文字を書き換える 

 

line = "metdtiaum" 

line = line.replace("t", "") 

print(line) 

 

------------------------------------------------------------------------------------------------------------------- 

 

引数：実引数の順番が守られて渡される引数 

並び順の通りに引数を渡す(位置引数) 

 

def check_position(first, second, third): 

    print(f"first: {first}") 

    print(f"second: {second}") 

    print(f"third: {third}") 

check_position(1, 2, 3) 

 

出力：first: 1 

second: 2 

third: 3 

 

明示的に渡す（キーワード引数）： 

 

check_keyword(second=1, third=2, first=3) 

 

出力：first: 3 

second: 1 

third: 2 

 

しかし、位置引数とキーワード引数を混在するとエラーが発生するが、位置引数の後ろなら... 

例１： 

 

check_keyword(second=1, 2, 3)                           #   エアー 

 

例２： 

 

check_keyword(1, third=2, second=3) 

 

出力：first: 1 

second: 3 

third: 2 

 

 

仮引数にデフォルト値を設定： 

仮引数にデフォルト値を設定することができる 

デフォルト値が設定された仮引数に引数が渡されなかったとき、その仮引数にはデフォルト値が代入される 

関数定義の際に、関数名(仮引数1=デフォルト値1, ..., 仮引数n=デフォルト値n) のかたちでデフォルト値を設定する 

たとえば、次のコードを実行すると、仮引数 first には実引数として渡した 1 が代入され、仮引数 second, third にはそれぞれデフォルト値の 2, 3 が代入される 

 

仮引数を用意するときに、 

デフォルト値を設定されていない仮引数の後ろに書いたほうがエラーを起こさない 

 

def check_default(first, second=2, third=3): 

    print(f"first: {first}") 

    print(f"second: {second}") 

    print(f"third: {third}") 

 

check_default(1)               #   first: 1  second: 2  third: 3 

check_default(1, 20)               #   first: 1  second: 20  third: 3 

check_default(1, third=10)               #   first: 1  second: 2  third: 10 

 

 

仮引数の有効範囲： 関数と同様、仮引数はその仮引数が用意された関数のなかでのみ使うことができる 

 

def func(x): 

    print(x) 

func(1) 

print(x)               #   空値 

 

仮引数への再代入がおよぼす影響： 

実引数として、整数型、文字列型、タプル型など、値を変えることができないので、実引数として渡した値に影響がおよぶことはない 

リスト型、辞書型、集合型など、値を自由に変えることができるので、影響がおよぶことがある 

 

再帰呼び出し：関数のなかで、いまの関数とおなじ関数を呼び出すこと 

 

n から 0 までの整数をカウントダウンする 

 

def count_down(n): 

    print(n) 

    if n == 0: 

        return 

  

    count_down(n-1) 

  

【 考え方1 】 

count_down 関数では、仮引数 n の値を出力して、count_down 関数を実引数 n-1 で呼び出している 

n-1 で呼び出した count_down 関数でも同様の処理をおこなって、次の count_down 関数を呼び出す 

このサイクルが続くことで、n から延々とカウントダウンできる 

今回は 0 までカウントダウンしたいから、仮引数 n の値が 0 になったとき、return 文でリターンして、次の count_down 関数を呼び出さないようにしている 

  

【 考え方2 】 

「count_down 関数 = 実引数として渡した値から 0 までの値を出力する関数」と意識する 

仮引数 n の値を出力して、count_down 関数を実引数 n-1 で呼び出せば、「n の値を出力」+「n-1 から 0 までの値を出力」となり、n から 0 までカウントダウンすることができる 

  

-- 

 

n から 0 までの整数をすべて足す 

和を求める： 

 

def rec_sum(n): 

    if n == 0: 

        return 0 

    return n + rec_sum(n-1) 

 

積を求める： 

 

def rec_product(n): 

    # 以下にコードを記述     

    if n == 0: 

        return 1 

    return n * rec_product(n - 1) 

     

【 考え方1 】 

rec_sum 関数では、仮引数 n の値と rec_sum(n-1) の返り値を足したものを return 文で返そうとする 

呼び出された rec_sum(n-1) では、n-1 と rec_sum(n-2) の返り値を足したものを return 文で返そうとする 

このサイクルが続くことで、n + n-1 + ... の値を求めることができるが、サイクルが続く限り、rec_sum(n), rec_sum(n-1), ... の値が確定しない 

今回は 0 までの和を求めたいから、仮引数 n の値が 0 になったとき、return 文で 0 を返して、次の rec_sum 関数を呼び出さないようにすることで、サイクルを止めて、rec_sum(1), rec_sum(2), ..., rec_sum(n-1), rec_sum(n) の値を確定させる 

  

【 考え方2 】 

「rec_sum 関数 = 実引数として渡した値から 0 までの値を返す関数」と意識する 

仮引数 n の値と rec_sum(n-1) の値を足せば、「n」+「n-1 から 0 までの和」となり、n から 0 までの和の値を求めることができる 

 

------------------------------------------------------------------------------------------------------------------- 

 

Join関数： 

 

 

------------------------------------------------------------------------------------------------------------------- 

 

モジュール理解： 

新規 py ファイルを作成し、ターミナルで実行する 

python3 test.py 

 

モジュールをインポート (import)：import 文を使うと、モジュールをインポートすることができる。 
「モジュールをインポートする」とは、他の py ファイルをコードのなかに取り込んで、その py ファイルに書かれているコードを利用できるようにすることを指す。 
import 文は import インポートしたいモジュールの名前 のように使う。 

testmod.py:    def hello(): 

                  print("Hello, World!") 

 

test.py:       import testmod 

 

testmod モジュールの hello メソッドを呼び出す際は testmod.hello と書く。 

test.py:       testmod.hello() 

 

モジュール内の関数をインポート (from import)： 

モジュールに定義されている特定の関数などを指定してインポートすることができる 

test.py:       from testmod import hello 

                  hello() 

 

インポートしたオブジェクトが代入される変数の名前を指定 (as)：as 節を使うとインポートしたオブジェクトが代入される変数名を指定することができる 

test.py:       import testmod as tm 

                  tm.hello() 

 

つまり、 

 

test.py:       from testmod import hello as h 

                  h() 

 

モジュール内の変数やクラスを利用：インポートしたモジュールに含まれる変数やクラスを利用することもできる 

 

testmod.py:   PI = 3.14 

class Circle: 

    def __init__(self, x, y, r): 

        self.x = x 

        self.y = y 

        self.r = r 

 

test.py:       from testmod import PI, Circle 

                  print(PI) 

                  c = Circle(0, 0, 5) 

                  print(c.x, c.y, c.r) 

 

複数のモジュールを一括で管理： 

複数のモジュールがまとめられたディレクトリのこと 

パッケージにまとめられたモジュールは、インポートできる 

カンマ区切りで複数のモジュールをインポートできる 

ただし、import a, b のようにインポートすることは推奨されていない　✖ 

ピリオドで区切って、モジュールまでのパスを入力する 

 

my_pacakage/my_module1:    def hello1(): 

                              print("Hello 1") 

my_pacakage/my_module2:    def hello2(): 

                              print("Hello 2") 

 

test.py:              from my_package import my_module1, my_module2 

  

my_module1.hello1() 

my_module2.hello2() 

  

from my_package.my_module1 import hello1 

from my_package.my_module2 import hello2 

 

hello1() 

hello2() 

 

my_module1 が my_package の属性ではないため、エラーが発生する 

 

test.py:              import my_package　✖✖✖ 

                      my_package.my_module1.hello1()　✖✖✖ 

 

 

モジュールの名前を確認 (__name__)： 

変数 __name__ には、モジュールの名前が代入される 

 

testmod.py:             def get_mod_name(): 

                           return __name__  

 

test.py:                print(__name__)                       #  __main__ 

                        import testmod 

                        print(testmod.get_mod_name())         #  testmod 

 

__mro__ を使ったときに出力された __main__ について： 

クラス名.__mro__ が示す値のなかには、__main__.StudentProgrammer のように、__main__ に続けてクラス名が書かれるクラスがあった 

__main__ は直接実行されているモジュールに付けられる特別な名前 

つまり、__main__.クラス名 は、クラス名 クラスが、直接実行されているモジュールの属性であることを示している 

 

class Person: 

    def __init__(self, name, age): 

        self.name = name 

        self.age = age 

  

    def add_age(self, year): 

        self.age += year 

 

class Programmer(Person): 

    def __init__(self, name, age, language): 

        super().__init__(name, age) 

        self.language = language 

        self.languages = {language} 

 

class StudentProgrammer(Programmer): 

    pass 

 

print(StudentProgrammer.__mro__)         #  <class `__main__.StudentProgrammer`>,  

                                            <class `__main__.Programmer`>,  

                                            <class `__main__.Person`> 

 

モジュールの処理を制御：直感実行以外は import された場合、直接実行されないように 

 

def func(): 

    print("func 関数が呼び出されました。") 

  

if __name__ == "__main__": 

    print("testmod が実行されました。") 

 

モジュールの利点： 

〇 異なるモジュールどうしで同じ変数名を使える 

〇 コードの再利用ができる 

 

 

標準ライブラリー： 

Random モジュール：疑似乱数に関するモジュール 

 

import random 

n = random.randint(1, 5) 

print(n) 

 

math モジュール：数学におけるさまざまな演算に関するモジュール 

 

import math 

x = math.sqrt(2) 

print(x)                           #   1.4142135623730951 

 

sys モジュール：実行システムに関するモジュール 

 

import sys 

sys.exit() 

print("paiza")                     #   空値 

 

------------------------------------------------------------------------------------------------------------------- 

 

例外・例外処理とはなにか： 

コード実行時に発生する例外に対しておこなう処理のこと 

例外処理を用意すると、例外によって実行が途中で終了しないようにすることができる 

 

 

複数の例外を受ける except 節： 

 

except (ValueError, ZeroDivisionError): 

    print("入力値は正しくりません。") 

 

または、 

 

except ValueError: 

    print("入力値は数字でなければなりません。") 

except ZeroDivisionError: 

    print("0 で割ることはできません。") 

 

例外クラスの継承関係と except 節：すべての例外は Exception の子孫なので、誘発しやすいから、具体的な例外をあげましょう 

 

print(ValueError.__mro__) 

print(ZeroDivisionError.__mro__) 

 

出力： 

(<class 'ValueError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>) 

(<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>) 

 

Python の BaseException クラスと Exception クラスはそれぞれ次のようなクラス 

BaseException: すべての例外クラスに継承されるクラス 

Exception: BaseException クラスのサブクラスで、ほとんどすべての例外クラスに継承されるクラス 

  

そして、それぞれのクラスは次のような意図で定義されている 

BaseException: すべての例外クラスの基底クラス 

Exception: システムの終了以外の例外クラス 

  

たとえば... 

SystemExit というクラスは Exception クラスを継承せずに、BaseException クラスを直接継承している 

SystemExit クラスは Python の実行を終了させるときに用いられる 

なぜ、Exception クラスを継承せずに、BaseException クラスを直接継承しているかというと、このクラスの例外が except Exception: といった except 節に誤って捕捉されないようにするため 

誤って捕捉されると、エラー出力がされないことがある 

 

例外クラスのインスタンスを生成： 

例外クラスのインスタンスのメンバ変数 args には、コンストラクタに渡した引数の分だけ要素をもつタプルが代入される 

 

e = ValueError("test1", "test2") 

print(e.args)                             #     ('test1', 'test2') 

 

 

例外を意図的に発生させる (raise)： 

例外クラスに渡した引数の値（= 例外クラスのインスタンスのメンバ変数 args の値）は、エラーメッセージに使われる 

 

raise 例外クラスのインスタンス 

raise ValueError 

 

この場合、メンバ変数 args の値を設定できないため、「なぜエラーが発生したか」を詳細に伝えることができない 

 

独自の例外クラスを定義： 

Exception クラスを継承してクラスを定義すると、独自の例外クラスを定義することができる 

 

class InputValueError(Exception): 

    pass 

try: 

    n = input() 

    if not n.isdigit(): 

        raise InputValueError("入力値は整数値でなければなりません。") 

    n = int(n) 

    print(n) 

except InputValueError as e: 

    print(e) 

 

------------------------------------------------------------------------------------------------------------------- 

 

オブジェクトとはなにか： 

「オブジェクト」は抽象的で、幅広く使われる 

例: 

整数の 1 

文字列の "paiza" 

関数の print 

モジュールの random 

 

「オブジェクト」は「型」をもち、「型」に応じた値をもつ  

オブジェクトの識別には id 関数によって得られる識別値が用いられる 

 

オブジェクトのid： 

id を変えずに値を変えることができないオブジェクトと、id を変えずに値を変えることができるオブジェクトの 2 種類がある 

 

def show_abc_id(a, b, c): 

    print(f"a: {id(a)}") 

    print(f"b: {id(b)}") 

    print(f"c: {id(c)}") 

 

a, b, c = 1, [0, 3, 6], (1, "apple") 

show_abc_id(a, b, c) 

 

print("=" * 3) 

 

a += 1 

b += [9, 12] 

c += ("cherry", "donut") 

show_abc_id(a, b, c) 

 

出力： 

 

a: 190766699688928 

b: 91699123514240 

c: 91699123967936 

=== 

a: 190766699688960 

b: 91699123514240 

c: 91699124097072 

 

イミュータブルなオブジェクト： 

id を変えずに値を変えることができないオブジェクトを「イミュータブルなオブジェクト」と言う 

つまり、イミュータブルなオブジェクトは、その値が常に同じであるオブジェクト 

たとえば、次のコードでは変数 a の示すオブジェクトの id が再代入前後で変わる 

 

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

 

a = 1 

show_id("更新前の a", a) 

 

a += 1 

show_id("更新後の a", a) 

 

出力： 

更新前の a: 188907653280736 

更新後の a: 188907653280768 

 

a += 1 で、変数 a の示すオブジェクトの値を変更しようとする 

すると、再代入前後で変数 a の示すオブジェクトの id が変わる 

オブジェクトは、その id によって識別されるため、再代入前後で変数 a の示すオブジェクトが変わったことがわかる 

 

別途： 

文字列はイミュータブルなオブジェクト 

 

a = "paiza" 

a[3] = "Z" 

print(a)                           #   エラー発生 

 

タプルはイミュータブルなオブジェクト 

 

a = ("apple", 120) 

a[1] = 145 

print(a)                           #   エラー発生 

 

 

ミュータブルなオブジェクト： 

id を変えずに値を変えることができるオブジェクトを「ミュータブルなオブジェクト」と言う 

つまり、ミュータブルなオブジェクトは。その値が変動しうるオブジェクト 

たとえば、次のコードでは変数 a の示すオブジェクトの id が再代入前後で変わらない 

 

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

 

a = [1, 2, 3] 

show_id("更新前の a", a) 

 

a += [4, 5, 6] 

show_id("更新後の a", a) 

 

a += [4, 5, 6] で、変数 a の示すオブジェクトの値を変更しようとする 

再代入前後で変数 a の示すオブジェクトの id が変わらなかったことがわかる 

オブジェクトは、その id によって識別されるため、再代入前後で変数 a の示すオブジェクトが変わらなかったと言える 

ミュータブルなオブジェクトは、同じ値をもつオブジェクトどうしでも、id が異なることがある 

  

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

 

b, c = [1, 2, 3], [1, 2, 3] 

show_id("リスト 1", b) 

show_id("リスト 2", c) 

 

出力： 

 

更新前の a: 87309480815488 

更新後の a: 87309480815488 

リスト 1: 87309481383872 

リスト 2: 87309481384320 

 

idと変数と代入： 

 

id を用いると、変数と代入を次のように考えることができる 

代入: 変数にオブジェクトの id を教えること 

変数: 代入時に教わった id を覚えているもの 

 

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

 

a = [1, 2, 3] 

b = a 

show_id("最初に生成した a", a) 

show_id("a が代入された b", b) 

 

出力： 

 

最初に生成した a: 100686518807424 

a が代入された b: 100686518807424 

 

ミュータブルなオブジェクトは、同じ値のオブジェクトどうしで id が異なることがある 

しかし、今回変数 b に代入されたオブジェクトの id は変数 a が示すものと同じであることがわかる 

このことから、変数への代入は、オブジェクトの id を変数に教えること、と考えることができる 

つまり、代入とは変数にオブジェクトを入れることではなく、どのオブジェクトを示すようにするかを変数に指定することと言える 

 

イミュータブルなオブジェクトが代入された変数： 

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

  

a = 1 

b = a 

  

a += 1 

print(b)                           #   1 

 

1 が出力されるのは、変数 a と b に代入されたオブジェクトがイミュータブルなオブジェクトだから 

b = a で変数 b は、この時点で変数 a が示すオブジェクトを教わる 

a += 1 で変数 a の示すオブジェクトは、値が 2 である別のオブジェクトに変更されるが、変数 b の示すオブジェクトが変更されるわけではない 

変数 b は、変数 a を見ているわけではなく、自身に代入されたオブジェクトを見ている 

これらのことは、id を使って確認できる 

  

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

  

a = 1 

b = a 

show_id("更新前の a", a) 

show_id("b", b) 

  

a += 1 

show_id("更新後の a", a) 

show_id("b", b) 

print(b) 

 

出力： 

 

更新前の a: 191416540836864 

b: 191416540836832 

更新後の a: 191416540836896 

b: 191416540836832 

1 

 

ミュータブルなオブジェクトが代入された変数： 

再代入は累算代入を除いて、オブジェクトの値を変更するわけではなく、変数が示すオブジェクトを変更する行為なので、他の変数が示す値は変わらない 

 

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

 

a = [1, 2, 3] 

b = a 

c = [1, 2, 3] 

show_id("更新前の a", a) 

show_id("b", b) 

show_id("c", c) 

 

a = a + [4] 

 

show_id("更新後の a", a) 

show_id("b", b) 

show_id("c", c) 

 

print(b) 

print(c) 

 

出力： 

 

更新前の a: 78458674277248 

b: 78458674277248 

c: 78458674737792 

更新後の a: 78458674740416 

b: 78458674277248 

c: 78458674737792 

[1, 2, 3] 

[1, 2, 3] 

 

累算代入の際は変数に代入されているオブジェクトの id を可能な限り変えずに値を変更するように演算がおこなわれる 

 

a = [1, 2, 3] 

b = a 

c = [1, 2, 3] 

show_id("更新前の a", a) 

show_id("b", b) 

show_id("c", c) 

 

a += [4] 

 

show_id("更新後の a", a) 

show_id("b", b) 

show_id("c", c) 

 

print(b) 

print(c) 

 

出力： 

 

更新前の a: 98529627532160 

b: 98529627532160 

c: 98529627992704 

更新後の a: 98529627532160 

b: 98529627532160 

c: 98529627992704 

[1, 2, 3, 4] 

[1, 2, 3] 

 

関数の引数： 

関数の仮引数の渡され方 

一般的に関数に引数が渡されるとき、その渡され方は次の 2 通りがある 

値渡し: オブジェクトがコピーされて渡されるような方法 

参照渡し: オブジェクトの id が渡されるような方法 

関数の内側と外側、どちらで id 関数を使っても得られる id が同じ 

Python は参照渡し： 

 

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

 

a = [1, 2, 3] 

print(f"関数の外: {id(a)}") 

show_id("関数の中", a) 

  

出力： 

 

関数の外: 102337650944896 

関数の中: 102337650944896 

 

-- 

 

関数内の処理が与える影響： 

関数内の処理は、関数の外のミュータブルなオブジェクトに影響を与えることがある 

twice 関数を呼び出した前後で、リスト a の要素が変わっている 

 

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

 

def twice(li): 

    for i in range(len(li)): 

        li[i] *= 2 

 

a = [1, 2, 3] 

print(f"関数処理の前: {a}") 

twice(a) 

print(f"関数処理の後: {a}") 

 

出力： 

 

関数処理の前: [1, 2, 3] 

関数処理の後: [2, 4, 6] 

 

-- 

 

対して、イミュータブルなオブジェクトについては影響がでない： 

increment 関数を呼び出した前後で、変数 n の示す値が変わらない 

 

def show_id(name, value): 

    print(f"{name}: {id(value)}") 

 

def increment(x): 

    x += 1 

    print(x) 

 

n = 813 

increment(n) 

print(n) 

 

出力： 

 

814 

813 

 

------------------------------------------------------------------------------------------------------------------- 

 

permutations：並べ替え（順列）をすべて作るための関数 

 

from itertools import permutations 

for p in permutations([1, 2, 3]): 

 print(p) 

 

出力： 

(1, 2, 3) 

(1, 3, 2) 

(2, 1, 3) 

(2, 3, 1) 

(3, 1, 2) 

(3, 2, 1) 

 

cmp_to_key：比較関数 

自分で比較ルールを作って sort() や sorted() に渡したいときに使う 

普通の並び替えなら、文字列としての辞書順 

 

from functools import cmp_to_key 

A = ["1", "20", "100"] 

print(sorted(A)) 

 

出力： 

['1', '100', '20'] 

 

その①（特殊なルール）：整数 

 

from functools import cmp_to_key 

def cmp(a, b): 

    return b - a 

A = [3, 1, 4, 2] 

A.sort(key=cmp_to_key(cmp)) 

print(A) 

 

出力： 

[4, 3, 2, 1] 

 

その②（特殊なルール）：文字列 

 

from functools import cmp_to_key 

def cmp(a, b): 

    if a + b > b + a: 

        return -1 

    elif a + b < b + a: 

        return 1 

    else: 

        return 0 

A = input().split() 

A.sort(key=cmp_to_key(cmp)) 

print("".join(A)) 

 

出力： 

201100 

```