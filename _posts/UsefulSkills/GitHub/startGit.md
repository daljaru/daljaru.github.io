### Git 시작하기

VCS(Version Control System) : 버전 관리 시스템

 1 : 프로젝트 되돌리기

 2 : 시간에 따른 변경사항 검토하기

 3 : 마지막 수정자 확인 등등..



깃의 데이터는 파일 시스템의 스냅샷이라 할 수 있으며 크기가 아주 작다. 

파일이 달라지지 않으면 Git은 성능을 위해서 파일을 저장하지 않는다. 이전 상태의 파일에 대한 링크만 저장한다. 



로컬에서 거의 모든 명령을 실행한다. 

체크섬으로 데이터를 관리.   > 무결성 보장. 



Git은 데이터를 추가할 뿐이다. 



#### Git이 사용하는 상태 3가지 

**Committed, Modified, Staged**



Committed : 데이터가 로컬 데이터베이스에 안전하게 저장됐다는 것을 의미.

Modified : 수정한 파일이 아직 로컬 데이터베이스에 Committed되지 않은 상태

Staged : 현재 수정한 파일을 곧 Commit할 것이라고 표시한 상태.

<img src=".\startGitimg\1.png" alt="1" style="zoom:60%;" />

Git directory : Git이 프로젝트의 메타데이터와 객체 데이터베이스를 저장하는 곳.

Working directory : 프로젝트의 특정 버전을 Checkout 한 것. Git디렉토리는 지금 작업하는 디스크에 있고 그 디렉토리에 압축된 데이터베이스에서 파일을 가져와서 Working directory를 만든다. 

Staging Area : Git 디렉토리에 있으며 곧 Commit할 파일에 대한 정보를 저장한다. Index라고 불리기도 함.



주요 활동.

- 워킹 디렉토리에서 파일을 수정한다.
- Staging Area에 파일을 Stage해서 커밋할 스냅샷을 만든다.
- Staging Area에 있는 파일들을 커밋해서 Git 디렉토리에 영구적인 스냅샷으로 저장한다.

Git 디렉토리에 있는 파일들은 Committed 상태. 

파일을 수정하고 Staging Area에 추가했다면 Staged이다. 

Checkout하고 나서 수정했지만, 아직 Staging Area에 추가하지 않았으면 Modified이다. 



### Git 최초 설정

'git config'라는 도구로 설정 내용을 확인하고 변경할 수 있다. Git은 이 설정에 따라 동작한다. 이때 사용하는 설정 파일은 세 가지나 된다.

- `/etc/gitconfig` 파일: 시스템의 모든 사용자와 모든 저장소에 적용되는 설정이다. `git config --system` 옵션으로 이 파일을 읽고 쓸 수 있다.
- `~/.gitconfig` 파일: 특정 사용자에게만 적용되는 설정이다. `git config --global` 옵션으로 이 파일을 읽고 쓸 수 있다.
- `.git/config`: 이 파일은 Git 디렉토리에 있고 특정 저장소(혹은 현재 작업 중인 프로젝트)에만 적용된다. 각 설정은 역순으로 우선시 된다. 그래서 `.git/config`가 `/etc/gitconfig`보다 우선한다.

윈도용 Git은 `$HOME` 디렉토리(`%USERPROFILE%` 환경변수)에 있는 `.gitconfig` 파일을 찾는다. 



##### 사용자 이름과 이메일 주소 설정

$ git config --global user.name "name"

$ git config --global user.email "emailName@example.com"



##### 편집기 설정  - 기본적으로 vi나 vim

만약 Emacs나 gedit같은 다른 편집기를 이용하고 싶을 경우에는 아래와 같이 설정.  

$ git config --global core.editor emacs



##### Diff도구

Merge충돌을 해소하기 위해 사용하는 Diff도구설정

$ git config --global merge.tool vimdiff    <- vimdiff를 쓸 경우. 

kdiff3, tkdiff, meld, xxdif, emerge, vimdiff, gvimdiff, ecmerge, opendiff등을 사용할 수 있다. 



##### 설정 확인

git config --list

<img src=".\startGitimg\2.png" alt="2" style="zoom:60%;" />



Git은 같은 키를 여러 파일에서 읽어오기 때문에 같은 키가 여러개가 있을 수 있다. 

##### 특정 Key값 확인하기

$ git config {key}

.![3](.\startGitimg\3.png)

##### 도움말 보는 방법

$ git help <verb>

$ git <verb> --help

$ man git-<verb>

.<img src=".\startGitimg\4.png" alt="4" style="zoom:80%;" />

<img src=".\startGitimg\5.PNG" alt="5" style="zoom:60%;" />.



### Git 저장소 만들기

**1: 기존 프로젝트를 Git저장소로 만드는 방법**

**2: 다른 서버에 있는 저장소를 Clone하는 방법.**



**기존 프로젝트를 Git 저장소로 만들기** > 해당 디렉토리로 이동 후 git init명령 실행

$ git init

이 명령은 .git이라는 하위 디렉토리를 생성.

![6](.\startGitimg\6.PNG)



저장소에 파일 추가하고 커밋.

$ git add sample.txt

![7](.\startGitimg\7.PNG)



**다른 저장소에 있는 저장소를 Clone** > git clone [url]명령어를 사용.

서버에 있는 모든 데이터를 복사한다. 

프로젝트 히스토리를 전부 받아온다. 

$ git clone [url]

![8](.\startGitimg\8.PNG)

git clone 명령은 grit이라는 디렉토리를 생성. 그 안에 .git디렉토리를 생성.

그리고 git 디렉토리에 서버의 가장 최신 버전을 Clone한다. 

* $ git clone [url] [otherName]   > otherName으로 Clone실행.

Git은 다양한 프로토콜을 지원. git::뿐만 아니라 http(s)://도 지원가능. ssh프로토콜도 지원가능하다. 



### 수정하고 저장하기.

파일을 수정하고 파일의 스냅샷을 Commit한다. 

Working Directory의 파일을 크게 Tracked(관리대상)과 Untracked(관리대상이 아님)으로 나뉜다. 

Tracked : 이미 스냅샷에 포함돼 있던 파일. **Unmodified, Modified, Staged** 상태 중 하나이다. 

Untracked : 그 외 나머지 파일.

![9](.\startGitimg\9.PNG)



#####  파일의 상태 확인하기   git status

$ git status

git clone 직후의 상태 : untracked 상태.

untracked상태라는 말의 의미 : 아직 스냅샷(Commit)에 넣어지지 않은 파일. Tracked상태가 되기 전까지 Git은 이 파일을 Commit하지 않는다. ex) 일하면서 생성하게 되는 바이너리 파일같은 것을 무심코 Commit하는 실수는 하지 않게 된다.

![10](.\startGitimg\10.PNG)



git add 명령어를 통해 파일을 추적하며 tracked상태로 넘어간다.  아래의 경우는 tracked상태이면서 staged상태로 넘어간 것을 의미한다. 

![11](.\startGitimg\11.PNG)



##### 이미 Tracked인 파일을 수정하기. 

tracked상태인 grit/디렉토리의 History.txt파일을 수정한 후 $ git status를 입력한다. 

tracked상태이지만 Staged상태가 아니라고 나오는 것을 확인 할 수 있다. 

![12](.\startGitimg\12.PNG)



add 명령어를 통해 Staged상태가 되게 만들어준다. 

![13](.\startGitimg\13.PNG)

위 두 예제를 통해 git add명령어는 새로 생긴 파일(untracked)을 tracked, staged 상태로 만들어 주고

또한 변경된 파일(tracked이지만 unstaged상태인)을 staged상태로 만들어줌을 확인할 수 있다. 



git commit을 실행하여 Commit해준다.

![14](.\startGitimg\14.PNG)



파일에서 위로 올라간 후 git status를 입력하면 아래와 같이 뜬다. 

![15](.\startGitimg\15.PNG)



tracked, staged 디렉토리에서  하위 디렉토리로 들어가 > 수정 후 해당 폴터를 commit했으므로 

상위 폴더의 스냅샷에서는 아직 전체적으로 Commit이 된 상태가 아니므로 위와 같이 뜨는 것이다. 

**git add 나 git checkout** 으로 staged상태로 통일해준다. 

![16](.\startGitimg\16.PNG)

Commit시킨다.

![17](.\startGitimg\17.PNG)

tree가 clean한 것을 확인 할 수 있다. 

* 그리고 git은 마지막 git add명령어를 실행한 것을 commit하기 때문에 수정을 했으면 반드시 git add를 하는 것을 잊지 말아야 한다. 



#### 파일 무시하기

어떤 파일은 Git이 자동으로 추가하거나 Untracked파일이라고 보여줄 필요가 없다. ex) 로그파일이나 발드 시스템이 자동으로 생성한 파일이 그렇다. 이러한 파일을 무시하려면 .gitignore파일을 만들고 그 안에 무시할 파일 패턴을 적는다.

ex

$ cat .gitignore

*.[oa]    > .o나 .a 확장자를 가진 파일을 무시.  (빌드 시스템이 만들어내는 오브젝트와 아카이브 파일)

*~   > ~로 끝나느 모든 파일 무시. (Emacs나 VI같은 텍스트 편집기가 임시로 만들어내는 파일)

log, tmp, pid같은 것들도 추가할 수 있다. 



.gitignore파일은 보통 처음에 만들어 두는 것이 편리하다.  > 실수로 Commit하는 일을 방지.

##### .gitignore파일에 입력하는 입력패턴 규칙

- 아무것도 없는 줄이나, `#`로 시작하는 줄은 무시한다.
- 표준 Glob 패턴을 사용한다.
- 디렉토리는 슬래시(`/`)를 끝에 사용하는 것으로 표현한다.
- 느낌표(`!`)로 시작하는 패턴의 파일은 무시하지 않는다.



 Glob패턴이란? 

정규표현식을 단순하게 만든 것. 보통 쉘에서 많이 사용. 

ex)

##### 확장자가 .a인 파일 무시
*.a
##### 윗 줄에서 확장자가 .a인 파일은 무시하게 했지만 lib.a는 무시하지 않는다.
!lib.a

##### 루트 디렉토리에 있는 TODO파일은 무시하고 subdir/TODO처럼 하위디렉토리에 있는 파일은 무시하지 않는다.

/TODO
##### build/ 디렉토리에 있는 모든 파일은 무시한다.
build/
##### `doc/notes.txt`같은 파일은 무시하고 doc/server/arch.txt같은 파일은 무시하지 않는다.
doc/*.txt
##### `doc` 디렉토리 아래의 모든 .txt 파일을 무시한다.
doc/**/*.txt



### 파일의 변경된 내역 확인하기 -  git diff

어떤 라인이 추가됐거나 변경됐는지 확인할 때 용이.

sample.txt파일을 수정하고 add   >  tracked, staged상태로 만들고

sample2.txt파일을 생성해서 add 후 수정한다. > tracked, unstaged상태로 만든다. 

![18](.\startGitimg\18.PNG)

git diff를 실행해서 상태를 확인한다. 

![19](.\startGitimg\19.PNG)

git diff는 unstaged상태인 것들만 보여준다.  수정하고 staged상태로 만들었다면 git diff는 아무것도 보여주지 않는다. 

다음은 sample2.txt를 add 후 git diff를 실행한 화면.  > 아무것도 나오지 않는다. 

![20](.\startGitimg\20.PNG)

다시 sample2.txt를 수정하여 modified, unstaged상태로 만든 후 git diff실행한 화면. 

![21](.\startGitimg\21.PNG)

추가한 것이 "testting new version" 텍스트임을 확인할 수 있다. 



만약 staged상태로 만들로 diff명령어로 차이를 확인하고 싶을 때는 git diff --cached명령어로 확인 할 수 있다.  여기서는 마지막에 git add된 상태로 확인 할 수 있다. 

![22](.\startGitimg\22.PNG)

#### 변경사항 Commit하기 - git commit

staged상태의 파일을 commit한다. 



$ git commit을 하면 Git 설정에 지정된 편집기가 실행된다.   -m을 통해 인라인으로 메세지를 집어넣을 수 있다. 

![23](.\startGitimg\23.PNG)

master branch에 commit했고 체크섬이 b494e7a임을 확인 할 수 있다. 바뀐 파일이 2개이며 삭제됐거나 추가된 줄이 몇 줄인지 알려준다. 

staging area에 있는 것만 commit하기 때문에 수정을 하고 staged상태에 넣지 않은 것은 다음에 commit할 수 있다. (VCS의 이점!)



##### staging area생략하기    git commit -a

staging area에 넣는 것이 불필요 할 때 사용한다. tracked상태의 파일을 자동으로 staging area에 넣는다.  >>  git add명령어를 쓸 필요가 없다!!

![24](.\startGitimg\24.PNG)

![25](.\startGitimg\25.PNG)

#### 파일 삭제하기   git rm

$ git rm명령어로 tracked파일을 삭제할 수 있다. (Staging Area에서 삭제하는 것이다.) 이 명령은 Working Directory에 있는 파일도 삭제하는 것이기 때문에 실제 파일도 삭제가 된다. 



만약 Git으로 삭제하지 않고 파일 삭제후 Git으로 git status를 통해 확인을 하면(혹은 rm명령어를 통해서 파일을 삭제하고 나면) Changes not staged for commit (Unstaged)상태임을 확인 할 수 있다. 

![26](.\startGitimg\26.PNG)

git rm sample.txt를 통해 staged상태로 만들어준다. 

![27](.\startGitimg\27.PNG)

실제로도 지워진 상태이다.

![28](.\startGitimg\28.PNG)



Commit을 하면 파일은 (시스템상에서)삭제되고 Git은 이 파일을 더이상 추적하지 않는다. 

![29](.\startGitimg\29.PNG)



##### Staging Area에서만 제거하고 Working Directory에는 그냥 남기는 방법이 있다. 

.gitignore 파일에 추가하는 것을 빼먹었거나 .a 파일을 실수로 추가했을 때 쓴다. --cached옵션을 사용한다. 

아래와 같이 sample2.txt를 Staging Area에서만 제거한다. 

$ git rm --cached sample2.txt

![30](.\startGitimg\30.PNG)

![31](.\startGitimg\31.PNG)

폴더에도 그대로 남아있는 것을 확인 할 수 있다. 

![32](.\startGitimg\32.PNG)



하지만 이렇게 Staging Area에서 삭제된 파일은 계속 Untracked files라고 스냅샷에 남아있는 것을 확인 할 수 있다. 

다시 실험을 위해 git add, git commit를 해준다. 

------------------------------------------



여러 개의 파일이나 디렉토리를 한꺼번에 삭제할 수 있다.  git rm명령어에 file-glob패턴을 사용한다. 

ex) $ git rm log/\*.log

$ git rm \*~



#### 파일 이름 변경하기

Git은 파일 이름 변경을 명시적으로 관리하지 않는다. 그러나 파일이름이 변경된 것을 알 수 있는 방법이 있다. 

아래와 같이 git mv명령을 통해 파일 이름을 변경할 수 있다. 

![33](.\startGitimg\33.PNG)

git status를 통해 파일 이름이 바뀐 것을 확인 할 수 있다. 

git commit을 하면 명시적으로 rename이라고 말해주고 있다. 

![34](.\startGitimg\34.PNG)



### 커밋 히스토리 조회하기

Git에는 히스토리를 조회하는 명령어인 git log가 있다. 

샘플 프로젝트를 clone한다. 

![35](.\startGitimg\35.PNG)

git add 후 해당 디렉토리로 들어가서 git log를 실행한다.

![36](.\startGitimg\36.PNG)

가장 최근에 commit한 기록부터 차례대로 보여주고 있는 것을 확인 할 수 있다. 

##### git log 의 옵션

-p : **각 Commit의 diff의 결과들을 보여준다**. -number은 number개수의 최근 결과들을 보여준다. 

git log -p -2

![37](.\startGitimg\37.PNG)



**히스토리를 단어단위로 보고 싶을 때**

git log -U1 --word-diff

![38](.\startGitimg\38.PNG)



**히스토리의 통계롤 보고 싶을 때** : --stat

git log --stat

![39](.\startGitimg\39.PNG)

 	각 파일별로 얼마나 많이 추가됐는지 확인할 수 있다. 



**log의 내용을 보여줄 때 기본 형식 이외에 여러 가지 중에 하나를 선택하기** :  --pretty

--pretty=oneline|short|full|fuller

![40](.\startGitimg\40.PNG)

![41](.\startGitimg\41.PNG)

![42](.\startGitimg\42.PNG)

![43](.\startGitimg\43.PNG)



**나만의 포맷으로 결과를 출력하고 싶을 때** : --pretty=fuller

![44](.\startGitimg\44.PNG)

![45](.\startGitimg\45.PNG)



**Branch와 Merge 히스토리를 보여주는 아스키 그래프 출력하기** : --pretty=format:%h %s" --graph

예시 : 

![46](.\startGitimg\46.PNG)



##### git log 의 다양한 옵션들(사진)

![47](.\startGitimg\47.PNG)

##### 조회를 제한하는 옵션: 

1. -<n> : 최근 n개의 Commit
2. --since  | --until : 시간을 기준으로 조회하기    ex) $ git log --since=2.weeks
3. --author : 저자를 지정하여 검색
4. --grep : Commit메세지에서 키워드를 검색 > 여러개 사용하면 그 중 하나 이상 만족하는 Commit을 찾는다. 모두 만족하는 Commit을 찾으려면 --all-match를 사용.
5. --path : 파일의 경로로 찾는다.  ex) git log -- path1 path2
6. ![48](.\startGitimg\48.PNG)





### 되돌리기

우리가 한 일을 되돌리려면???

주의할 점 : 되돌리면 다시 복구할 수 없다. 



##### Commit수정하기

완료한 Commit을 수정하고 싶을 때(너무 일찍 Commit했거나, 파일을 빼먹었을 때, Commit Message를 잘못 적었을 때)   :  --amend

$ git commit --amend



아래와 같이 untracked파일 하나를 같이 commit하는 것을 깜빡했을 때.

![49](.\startGitimg\49.PNG)



untracked파일인 sample.txt를 tracked, staged상태로 만들어 주고

git commit --amend를 실행하면 sample.txt파일이 이전에 Commit한 파일들과 같이 Commit가 된다.  이전의 Commit이 덮어씌워지게 된다. 

![50](.\startGitimg\50.PNG)



##### 파일 상태를 Unstaged로 변경하기 (Untracked로..)

아래와 같이 test1.txt만 add하고 싶은데 실수로 add*를 해버렸을 경우의 이야기다. 

![51](.\startGitimg\51.PNG)



화면에 git reset HEAD <file>....을 볼 수 있는데 이것으로 Unstaged로 변경할 수 있다. 

$ git reset HEAD test2.txt

![52](.\startGitimg\52.PNG)



##### Modified한 파일 되돌리기

아래와 같이 test1.txt파일을 수정하고 상태를 확인해보았다. 

![53](.\startGitimg\53.PNG)

git checkout -- <file>....을 볼 수 있는데 이 것이 modified를 되돌리는 명령이다. 

![54](.\startGitimg\54.PNG)

test1.txt파일도 수정하기 전의  빈 내용으로 바뀐것을 확인할 수 있었다.

![55](.\startGitimg\55.PNG)



하지만 이 방법은 수정했던 내용을 전부 없애버리기 때문에 위험한 경우에 해당한다. 신중히 써야한다. 



### 리모트 저장소 활용하기

대표적인 리모트 저장소로 Github를 예로 들 수 있다. 

다른 사람과 같이 일하면서 그곳에 데이터를 Push, Pull하는 것이다. 

저장소를 추가, 삭제하는 것.

브랜치를 관리하고 추적할지 말지 등을 관리하는 것.



##### 리모트 저장소 확인하기 :  git remote

git remote로 현재 프로젝트에 등록된 리모트 저장소를 확인할 수 있다. 

간단하게 다음과 같이 repository를 Github에 만들고 실험해보자. 

![56](.\startGitimg\56.PNG)

![57](.\startGitimg\57.PNG)

해당 url로 git clone실행 후  디렉토리로 들어가 git remote를 실행한다. 

$ git remote

origin이라는 결과가 뜨는 것을 확인할 수 있다. 

옵션

-v : 단축이름과 url확인하기

![58](.\startGitimg\58.PNG)

origin에만 push할 수 있다. 





![59](.\startGitimg\59.PNG)

이게 뭔말인지 모르겠다...







#### 리모트 저장소를 pull하거나 Fetch하기

리모드 저장소에서 데이터 가져오기

$ git fetch [remote-name]

위 명령은 로컬에는 없지만 리모트 저장소에 있는 데이터를 전부 가져온다.  > 리모트 저장소의 모든 브랜치를 로컬에서 접근할 수 있어서 언제든지 Merge를 하거나 내용을 살펴볼 수 있다. 

저장소를 Clone하면 명령은 자동으로 리모트 저장소를 origin이라는 이름으로 추가한다. 

나중에 `git fetch origin`을 실행하면 Clone한 이후에(혹은 마지막으로 가져온 이후에) 수정된 것을 모두 가져온다. `fetch` 명령은 리모트 저장소의 데이터를 모두 로컬로 가져오지만, 자동으로 머지하지 않는다. 그래서 당신이 로컬에서 하던 작업을 정리하고 나서 수동으로 머지해야 한다.



그냥 쉽게 **git pull** 로 리모트 저장소에서 데이터를 가져오거나 자동으로 로컬 브랜치와 Merge할 수 있다. 

git clone명령은 자동으로 로컬의 master브랜치가 리모트 저장소의 master브랜치를 추적하도록 한다. 



#### 리모트 저장소에 Push하기

git push [remote repository name] [branch name] 으로 단순하다. 

master브랜치를 origin서버에 Push하려면 (Clone하면 자동으로 origin이름이 생성된다.) 아래와 같이 서버에 Push한다. 

$ git push origin master

아래와 같이 로컬에서 sample.txt파일을 만들고 Commit을 한 후 

![60](.\startGitimg\60.PNG)

git push origin master를 실행해보자.

![61](.\startGitimg\61.PNG)



실제로 gitHub에 repository에 sample.txt파일이 업로드 된 것을 확인할 수 있다. 

![62](.\startGitimg\62.PNG)



##### 리모트 저장소 살펴보기  : git remote show [remote repository name]

위 명령어로 리모트 저장소의 내용을 확인할 수 있다. 

![63](.\startGitimg\63.PNG)



##### 리모트 저장소의 이름 변경하기 : git remote rename fromName toName

위 명령어로 리모트저장소의 이름을 바꿀 수 있다. 

![64](.\startGitimg\64.PNG)