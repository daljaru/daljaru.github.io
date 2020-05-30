---
layout: post
title: "Gitlab-Collaboration"
date: 2020-04-27
desc: "How to collaborate team memeber with GitLab.."
keywords: gitlab, git, branch, master, push, pull, merge, conflict
categories: [Useful_Skills]
tags: [useful,collaboration,team,git,gitlab]
---

# GitLab으로 협업하기 

간단한 프로젝트를 진행하면서 **GitLab**과 **Git**을 이용해서 협력하는 방법을 배워봅시다. 프로젝트참여자가 **Project Manager** 1명,  **Developer**가 1명이 있다고 가정하겠습니다.(실제로는 Developer가 여러명이겠죠?)

Gitlab계정을 2개 생성해서 한 계정은 Project Manager용으로, 다른 하나는 Developer용으로 썼습니다. 그리고 각 역할이 어떤 일을 해야하는지 알기 위해 설명 전에 해당 **역할 이름**을 굵게 표시하였습니다.



## Groups, Projects, Members

### Project Manager

 Project Manager는 **Group**을 하나 만듭니다. Group은 Project들을 모아놓은 장소입니다. 멤버들과 여러 Project들을 관리할 수 있습니다.

![makeGroup](/static/assets/img/blog/usefulSkills/gitlabImages/makeGroup.png){: width="100%" height="100%"}



 GitLab에서 왼쪽 상단에 보면 Groups tab이 보입니다. Groups tab에서 화살표 -> Your groups을 클릭하면 위의 화면과 같이 자신의 그룹들이 보이는 창이 나타납니다. 현재 그룹이 하나도 없기 때문에 아무것도 표시되지 않고 있네요. 



이제 오른쪽 상단에 New group을 클릭합니다.

![makeGroup2](/static/assets/img/blog/usefulSkills/gitlabImages/makeGroup2.png){: width="100%" height="100%"}

* Group name에 그룹 이름을 설정합니다. 
* Group URL에는 Group name에서 설정한 이름 그대로 자동으로 들어가게 됩니다. 
* Group description에는 이 그룹에 대한 설명을 적습니다. 
* Group avatar는 그룹을 대표하는 이미지를 넣는 곳입니다. 
* **Visibility Level**은 공개범위를 설정하는 곳입니다. 자신의 프로젝트를 오픈소스로 활용하고 싶다면 Public으로 설정합니다. 전세계의 개발자들이 **Public** 프로젝트에 참여하고 코드를 개선할 수 있습니다. 멤버들끼리만 개발하는 소스로 활용한다면 **Private**로 설정합니다. 



설정을 마무리하고 Create Group을 클릭합니다.  

![newGroup](/static/assets/img/blog/usefulSkills/gitlabImages/newGroup.png){: width="100%" height="100%"}

그룹을 생성했다면 위과 같이 그룹의 메인화면으로 옮겨집니다. 오른쪽 상단에 New project 초록색 버튼이 보입니다. 이제 그룹을 생성했으니 프로젝트를 하나 만들 차례입니다.



New project를 클릭합니다. 

![makeProject](/static/assets/img/blog/usefulSkills/gitlabImages/makeProject.png){: width="100%" height="100%"}

* Blank project라고 빈 프로젝트를 생성하는 탭이 있습니다.

* Project name에 프로젝트 이름을 설정합니다. 
* Project URL에는 프로젝트 이름에 맞게 자동으로 설정이 됩니다. 
* Project description은 프로젝트에 대한 간단한 설명을 적습니다. 
* **Visibility Level**은 그룹을 Private로 설정했기 때문에 자동으로 Private으로 설정이 됩니다. 
* Initialize repository with a README 체크박스를 클릭합니다. README 마크다운 파일이 미리 생성됩니다. 보통 개발자들은 README마크다운 파일에 해당 프로젝트에 대한 상세한 설명을 적습니다.



설정을 마무리하고 Create project 버튼을 클릭합니다.

![projectCreated](/static/assets/img/blog/usefulSkills/gitlabImages/projectCreated.png){: width="100%" height="100%"}

Project 'First_OOP_Project'가 성공적으로 만들어졌다는 메시지와 함께 프로젝트 페이지가 로드됩니다. 현재 branch가 1개가 있고 master branch임을 확인할 수 있습니다.



### Branch에 대하여.. 간단한 설명

branch는 하나의 작업공간 혹은 파일시스템이라고 볼 수 있습니다. 우리는 First_OOP_Project를 만들면서 초기 작업공간의 상태인 master branch를 생성했습니다. 

![master](/static/assets/img/blog/usefulSkills/gitlabImages/master.png){: width="100%" height="100%"}

이 master branch에 프로젝트의 최종 완성본만 넣을 것입니다.

 Git과 같은 VCS(Version Control System)를 사용하면 개발자들이 프로젝트를 여러 작업 공간으로 나눠서 코딩 및 수정과정을 거쳐 병합할 수 있습니다. 

좀 더 구체적으로 말하면, 새로운 branch를 만드는 순간 기존 branch의 복사본이 파일시스템에 기록되는데 새로운 branch에서 작업을 진행하고 기존 branch로 병합하는 과정을 반복합니다. 이러한 과정 덕분에 Project version 관리가 용이합니다. 그리고 멤버들이 상호간 코드 비교를 수시로 하지 않아도 수정사항을 팀 멤버들과 공유할 수 있습니다.

![branch](/static/assets/img/blog/usefulSkills/gitlabImages/branch.png){: width="100%" height="100%"}

VCS를 잘 이용하면 아래와 같이 귀찮은 작업을 하지 않아도 됩니다.

.![complicateUpdate](/static/assets/img/blog/usefulSkills/gitlabImages/complicateUpdate.png){: width="100%" height="100%"}





### 다시 본론으로...

이제 Remote master branch에서 Remote premaster branch 하나 만들겠습니다.

![createBranch](/static/assets/img/blog/usefulSkills/gitlabImages/createBranch.png){: width="100%" height="100%"}

master > first_oop_project 오른쪽에 `+`버튼이 보입니다. `+`버튼으로 현재 디렉토리에 새로운 파일이나 폴더를 만들거나 파일업로드가 가능합니다. 또한 현재 branch에 연결된 새로운 branch나 tag생성이 가능합니다.



New branch를 클릭합니다.  ![newPremasterBranch](/static/assets/img/blog/usefulSkills/gitlabImages/newPremasterBranch.png){: width="100%" height="100%"}

새로운 branch를 만드는 화면이 로드됩니다. 

* Branch name에 새로 만들 branch이름을 적습니다.  premaster로 정하겠습니다.



Create branch버튼을 클릭합니다. 

![premasterCreated](/static/assets/img/blog/usefulSkills/gitlabImages/premasterCreated.png){: width="100%" height="100%"}



You **pushed** to premaster just now라는 메시지와 함께 premaster branch가 생성되었습니다. 

master branch에서 premaster branch를 방금 만든 상태이기 때문에 premaster branch는 master branch와 파일 구조가 똑같습니다. master branch와 동일하게 README.md파일밖에 없습니다.



이제 멤버들을 추가하면 프로젝트를 시작하기 위한 세팅이 끝납니다!

왼쪽 하단에 Settings탭에 Members 항목이 있습니다. 

![addMembers](/static/assets/img/blog/usefulSkills/gitlabImages/addMembers.png){: width="100%" height="100%"}



Members를 클릭합니다.

![inviteMembers](/static/assets/img/blog/usefulSkills/gitlabImages/inviteMembers.png){: width="100%" height="100%"}

* GitLab member or Email address 에서 멤버들을 검색해서 추가합니다.
* **Choose a role permission**에서 멤버들의 접근권한을 부여합니다. Developer들이 Merge 기능을 이용하기 위해 developer로 설정합니다. 



설정을 완료하고 Invite를 클릭합니다. `Users were succesfully added` 메시지가 뜹니다.

![inviteSuccess](/static/assets/img/blog/usefulSkills/gitlabImages/inviteSuccess.png){: width="100%" height="100%"}

이제부터 premaster branch에 PM과 developer가 프로그램파일들을 지속적으로 업데이트할 것입니다. 그리고  배포가 가능한 프로젝트가 되면 PM이 master branch와 merge작업을 하고 프로젝트가 최종완성됩니다. 



### 이제까지의 정리...

PM은 Gitlab에서 Remote reqository생성한다. > master branch가 생성된다.

master branch에서 premaster branch를 하나 만든다.

Member들을 추가한다.



## Clone, Branch update, Pull

### **Developer**

자 이제 Project Manager가 멤버들을 추가했습니다. 멤버들은 GitLab에 들어가면 자신의 프로젝트 목록에서First_OOP_Project를 확인할 수 있습니다.

![memberProject](/static/assets/img/blog/usefulSkills/gitlabImages/memberProject.png){: width="100%" height="100%"}





Your projects를 누르면 자신이 추가된 프로젝트가 뜹니다. 

![MemberYourProject](/static/assets/img/blog/usefulSkills/gitlabImages/MemberYourProject.png){: width="100%" height="100%"}



이제 여기서부터 대부분의 작업이 로컬에서 이루어집니다.



### 작업이 구체적으로 어떻게 이루어지나요?..간단한 설명

Developer의 작업방식은 아래와 같습니다.

![developRoute](/static/assets/img/blog/usefulSkills/gitlabImages/developRoute.png){: width="100%" height="100%"}

1번부터 5번까지의 과정을 PM과 Developer가 프로젝트가 완성되서 끝날 때까지 반복합니다.



### 다시 본론으로...

이제 Developer가 자신의 로컬환경으로 GitLab에 있는 Repository를 가져와야 합니다. 이 과정은 프로젝트 개발과정에서 한 번만 실행합니다.

Git을 실행합니다. 원하는 디렉토리를 만들어서 해당 디렉토리로 이동합니다. 

Remote repository를 자신의 로컬환경으로 가져오는 명령어는 git clone입니다. 

~~~
git clone 'repository url'
~~~

![developGitclone](/static/assets/img/blog/usefulSkills/gitlabImages/developGitclone.png){: width="100%" height="100%"}

subAccount라는 디렉토리를 만들고 해당 디렉토리 안에서 git clone명령어를 실행했습니다. 

Repository url은 GitLab에 있는 Repository에 가면 해당 Repository의 URL을 복사할 수 있는 Clone 버튼이 있습니다.

![developColoneButton](/static/assets/img/blog/usefulSkills/gitlabImages/developColoneButton.png){: width="100%" height="100%"}

 

~~~
git branch -a
~~~

위 명령어를 쳐볼까요. git branch -a를 치면 Local branch와 Remote branch 모두를 볼 수 있습니다. 

![gitBranchA](/static/assets/img/blog/usefulSkills/gitlabImages/gitBranchA.png){: width="100%" height="100%"}

초록색으로 표시된 것이 Local환경에 있는 branch들이고 빨간색이 Remote환경에 있는 branch들입니다. 우리가 GitLab사이트에서 premater branch를 만들었기 때문에 remotes/origin/premaster이 보입니다.



Local과 Remote의 branch가 만들어지고 지워지는 과정은 서로 독립적입니다. 반드시 **동기화**를 해야지만 서로의 branch가 같아진다는 점이 중요합니다.



로컬에도 premaster branch를 만들어두면 좋겠죠.

~~~
git checkout -b premaster
~~~

위 명령어로 premaster branch를 로컬에서 만들고 해당 branch로 이동합니다. 

![localNewPremaster](/static/assets/img/blog/usefulSkills/gitlabImages/localNewPremaster.png){: width="100%" height="100%"}



항상 작업을 시작하기 전에는 Remote의 branch 상태들과 동기화를 진행합니다.

~~~
git remote update
git fetch -p
~~~

![remoteUpdatePull](/static/assets/img/blog/usefulSkills/gitlabImages/remoteUpdatePull.png){: width="100%" height="100%"}



### 이제까지의 정리...

Developer는 **맨 처음만** : git clone 'repository url'

Local master branch에서도 원격과 똑같이 local premaster branch를 하나 만든다.(git checkout -b premaster)

Remote branch를  update한다. (git remote update, git fetch -p)





## Pull, Add, Commit

### **Developer (반복)**

자 이제 Remote Repository도 가져왔고 **이제 프로젝트가 끝날 때까지** Project Manager와 Developer가 작업하는 일만 남았습니다.

항상 작업을 시작하기 전에는 Remote의 branch 상태들을 **동기화**하고 Remote Repository에 **내가 모르는 파일들이 업데이트가 되었는지 확인**합니다.  앞 챕터에서 branch update를 했으므로 pull 작업을 해봅시다.



~~~
git pull origin master
~~~

![pull](/static/assets/img/blog/usefulSkills/gitlabImages/pull.png){: width="100%" height="100%"}

`git pull origin premaster`는 Remote에 있는 premaster branch에 있는 내용을 현재 로컬(premaster branch)와 병합한다는 의미입니다.   



참고로 origin은 remote에 있는 repository를 가리킵니다. `git remote -v`을 통해 확인할 수 있습니다. 

![originMeaning](/static/assets/img/blog/usefulSkills/gitlabImages/originMeaning.png){: width="100%" height="100%"}



이제 working branch를 하나 만들어봅시다. 당신이 login 클래스를 구현하는 역할을 담당했다고 가정합시다. Local premaster branch에서 새로운 branch를 만들어봅니다. 이름은 loginBranch로 하겠습니다.

~~~
git checkout -b loginBranch
~~~

git checkout 명령어를 통해 branch를 새로 만들고 해당 branch로 이동했습니다.

![loginbranch](/static/assets/img/blog/usefulSkills/gitlabImages/loginbranch.png){: width="100%" height="100%"}

.

시간이 흘러서 당신은 열심히 코딩작업을 통해 login 클래스를 구현했습니다.

.

![completeLogin](/static/assets/img/blog/usefulSkills/gitlabImages/completeLogin.png){: width="100%" height="100%"}



이제 add와 commit작업을 진행합니다.



### add와 commit에 대하여... 간단한 설명

Git을 사용하다보면 add, commit, push라는 명령어를 실행하게 될 것입니다. 이 세가지 명령어를 포장 및 배송업무에 비유를 해볼게요. 

당신에게 포장 및 배송해야할 물품들이 여러개가 있습니다. 이 물품들은 목적지로 배송해야하는데

* 이 물품등 중에서 포장해야할 물품들을 고르고
* 물품들을 포장한 다음에
* 목적지로 배송해야 합니다. 



당신이 여러개의 클래스들을 만들었다고 생각해봅시다. 이 클래스들은 Local에서 만들었으니 

* 이 클래스들 중에서 Remote와 연동을 할 파일들을 고르고  - add
* 파일들을 연동할 준비를 마쳐서  - commit
* Remote와 연동을 해야합니다.  - push



### 다시 본론으로...

포장 및 배송업 비유가 이해가 잘 되시나요?  직접 해보겠습니다. 

~~~
git status
git add 'filename'
or
git add .  (모든 파일을 add합니다.)

~~~



git status는 현재 파일시스템의 상태를 확인합니다. git status를 입력했더니 git에서 add할 파일이 있다고 알려줍니다. `git add Login.class`로 add를 진행하겠습니다. 

![add](/static/assets/img/blog/usefulSkills/gitlabImages/add.png){: width="100%" height="100%"}



~~~
git status
git commit -m "commit message"
~~~

git status를 입력했더니 이젠 commit할 파일이 있다고 알려줍니다.`git commit -m "Login class update"`로 commit을 진행하겠습니다. 

![commit](/static/assets/img/blog/usefulSkills/gitlabImages/commit.png){: width="100%" height="100%"}



### 이제까지의 정리...

Remote premaster branch로부터 pull작업 (git pull origin premaster)

Working branch를 하나 만들고(git checkout -b loginBranch)

작업 시작

.

작업이 끝나면 add와 commit을 실행해준다. (git add ., git commit -m "message")





## Conflict, Push, Merge request

### Developer

 이제 Remote에 push를 할 일만 남았습니다. 여기서 **중요한 문제**가 있습니다. 바로 **충돌**문제입니다. 당신이 프로젝트에서 담당한 코드를 작성하고 있을 때, 혹은 코드를 수정하고 있을 때 동료 개발자가 나와 똑같은 파일을 건들지 않았다는 보장이 없습니다. 

 당신이 pull작업으로 가져온 원본 파일을 수정하는 동안 Remote의 원본 파일이 이미 동료 개발자에 의해 Update된다면 어떻게 될까요?  

 당연히 push를 하는 과정에서 충돌이 발생합니다. '당신의 원본파일 생김새가 조금 이상하다, 원래 저렇게 안생겼는데...?'라는 메시지를 받게 됩니다. 

 하지만 걱정할 필요는 없습니다.  push를 하기 전에 conflict를 방지할 수 있습니다. 



**Verify conflict**

premaster branch로 이동합니다.

~~~
git checkout premaster
~~~



여기서 Remote의 premaster branch로부터 pull작업을 진행합니다.  만약 내가 작업했던 원본파일에 내가 모르는 업데이트가 있었다면 Local의 Login.class파일은 변경될 것입니다. 

~~~
git pull origin premaster
~~~



다시 loginBranch branch로 이동하고

~~~
git checkout loginBranch
~~~

Local premaster branch와 merge를 해봅시다.  Local premaster branch가 변경된 Login.class파일을 가지고 있다면 당연히 loginBranch branch의 Login.class와 merge가 안됩니다.

~~~
git merge premaster
~~~

![confilctOccur](/static/assets/img/blog/usefulSkills/gitlabImages/confilctOccur.png){: width="100%" height="100%"}

**(처음에는 당연히 충돌이 발생하지 않아서 설명을 위해 한번 다시 작업하느라 conflictBranch branch가 있는 것입니다. 설명은 loginBranch branch로 진행하겠습니다.)**



충돌이 발생했네요! 이제 충돌이 발생하지 않게 수정해야겠습니다. 한번 Login.class를 살펴볼까요. 

![conflictSolve](/static/assets/img/blog/usefulSkills/gitlabImages/conflictSolve.png){: width="100%" height="100%"}

​	

파일이 이상하게 변해있죠? 

~~~
<<<<<HEAD

내가 작성한 코드

=======

내가 모르는 새에 업데이트 된 코드

>>>>>>> premaster
~~~

======를 기준으로 HEAD쪽에 있는 코드가 내가 작성했던 코드이고 premaster쪽에 있는 코드가 동료 개발자의 코드입니다. 

이제 여기서 적절하게 수정을 해줍니다. 내 코드가 이상하면 HEAD쪽을 날려버리고 동료개발자 코드가 이상하면 premaster쪽을 날려버리면 되겠죠? 동료 개발자 코드를 날려버립시다. 

.![conflictSolve2](/static/assets/img/blog/usefulSkills/gitlabImages/conflictSolve2.png){: width="100%" height="100%"}



충돌이 일어나고 아직 merging중이라 loginBranch|MERGING이라는 표시가 뜨고 있습니다. 

![confilctMerging](/static/assets/img/blog/usefulSkills/gitlabImages/confilctMerging.png){: width="100%" height="100%"}



login.class 파일을 새로 수정했으므로 이제 다시 add와 commit을 진행합니다. 

![conflictSolve3](/static/assets/img/blog/usefulSkills/gitlabImages/conflictSolve3.png){: width="100%" height="100%"}



**휴... 이제 push를 하는 일만 남았네요!** 

~~~
git push --set-upstream origin loginBranch
~~~

![pushUpstream](/static/assets/img/blog/usefulSkills/gitlabImages/pushUpstream.png){: width="100%" height="100%"}

`git push --set-upstream origin loginBranch`는 origin에 loginBranch branch에 commit한 파일들을 기록합니다. 

현재 상태에서 remote에 loginBranch branch가 없었지만 위 명령어는 remote에 loginBranch branch를 자동으로 만들어주고 push를 진행합니다.

이제 push를 완료했으니 Project Manager나 동료 Member에게 코드리뷰를 하고 Remote에 premaster branch에 merge를 해달라고 요청합니다.



GitLab사이트로 가봅시다.  프로젝트의 Branch가 3개가 된것을 확인할 수 있습니다. 

![mergeRequest1](/static/assets/img/blog/usefulSkills/gitlabImages/mergeRequest1.png){: width="100%" height="100%"}



Branches를 눌러볼까요. 우리가 만들었던 loginBranch branch가 push를 통해 올려진 것을 확인할 수 있습니다.  

![branches](/static/assets/img/blog/usefulSkills/gitlabImages/branches.png){: width="100%" height="100%"}



loginBranch branch오른쪽에 있는 Merge request버튼을 눌러볼까요.

![mergeRequest2](/static/assets/img/blog/usefulSkills/gitlabImages/mergeRequest2.png){: width="100%" height="100%"}

위의 빨간색 박스에 주목해주세요. 우린 loginBranch branch에서 premaster branch로 merge를 하고 싶기 때문에 저렇게 설정을 하면 안됩니다. master branch에는 최종본만 올리려고 한다고 정했습니다. 



From loginBranch into premaster로 변경하기 위해 Change branches를 눌러봅시다. Source branch를 자신이 작업했던 loginBranch로, Traget branch를 premaster로 설정해줍시다. 

![mergeRequest3](/static/assets/img/blog/usefulSkills/gitlabImages/mergeRequest3.png){: width="100%" height="100%"}



Compare branches and continue를 눌러줍니다. 

![mergeRequest4](/static/assets/img/blog/usefulSkills/gitlabImages/mergeRequest4.png){: width="100%" height="100%"}

* Title에는 merge request의 제목을 적습니다. 
* Assignee는 이 Merge Request를 검토할 사람을 지정할 수 있습니다. 여기서는 PM에게 관리를 받을 것이기 때문에 관리자를 선택해줍시다. 
* Merge options에 `Delete source branch when merge request is accepted`가 보입니다. 현재 Remote에는 loginBranch branch가 생성되어 있죠. merge가 승인이 나면 이 branch를 Remote에서 지우겠다는 의미입니다.  



설정을 완료하고 Submit merge request를 누릅니다. 



### 이제까지의 정리...

**Confilict 확인**

Local premaster branch로 이동(git checkout premaster)

Remote premaster branch로부터 pull작업(git pull origin premaster)

Working branch로 이동(git checkout function)

Working branch를 Local premaster branch와 merge(git merge premaster)

**if isConfilict**

​	Code 비교 후 수정 작업을 진행

​	.

​	수정 작업이 끝나면 add와 commit을 실행해준다. (git add ., git commit -m "message")

Remote repository에 Local working branch를 push합니다. (git push --set-upstream origin loginBranch)

Remote repository에 자동으로 Remote working branch가 생성됩니다.

Gitlab 사이트에서 merge request를 진행합니다. Source는 working branch. Destination은 premaster branch로 지정합니다.



## Merge

### Project Manager

자 이제 merge request까지 했습니다. Developer는 PM에게 Merge request를 보냈으니 내 코드를 검토해달라고 요청했습니다. 이제 여기서 PM이 열일할 타이밍입니다. 



PM은 GitLab에서 Project Repository로 이동합니다. 

![OwnerMergeRequest](/static/assets/img/blog/usefulSkills/gitlabImages/OwnerMergeRequest.png){: width="100%" height="100%"}

Project Manager에게 Merge Request가 온것을 확인 할 수 있습니다. 오른쪽 상단에 보면 빨간 박스가 2개가 있죠. 왼쪽은 Merge request가 1건있다는 뜻이고 오른쪽은 나에게 할일이 생겼다는 뜻입니다. (Asignee를 PM으로 설정했기 때문에 발생하는 알림입니다.)



왼쪽 탭에서 Merge Request를 눌러봅시다. 

![OwnerMergeRequest2](/static/assets/img/blog/usefulSkills/gitlabImages/OwnerMergeRequest2.png){: width="100%" height="100%"}

어떤 Merge request가 있는지 확인할 수 있습니다. Developer가 적어둔 Merge request 제목이 보이네요. 



Login class update를 클릭합니다.

![OwnerMergeRequest3](/static/assets/img/blog/usefulSkills/gitlabImages/OwnerMergeRequest3.png){: width="100%" height="100%"}

좋아요 싫어요를 표시할 수 있고 Comment도 달 수 있습니다.! 오른쪽 위에`Close merge request`로 merge request를 거절할 수도 있습니다. 



Overview탭 오른쪽에 있는 Changes탭에서 작성한 코드들을 볼 수 있습니다.

![OwnerMergeRequest4](/static/assets/img/blog/usefulSkills/gitlabImages/OwnerMergeRequest4.png){: width="100%" height="100%"}



충돌이 일어난 파일이였다면 아래와 같이 뜹니다.

![OwnerconflictMergeRequest](/static/assets/img/blog/usefulSkills/gitlabImages/OwnerconflictMergeRequest.png){: width="100%" height="100%"}



이제 Merge버튼을 눌러줍시다. 

![merged](/static/assets/img/blog/usefulSkills/gitlabImages/merged.png){: width="100%" height="100%"}

Merge Request가 0개로 줄어든 것을 확인할 수 있습니다. 그리고 premaster branch로 옮겨보니 Login.class가 업데이트 된것을 확인할 수 있네요!



### 이제까지의 정리...

Gitlab 사이트에서 Owner가 Merge Request를 확인하고 코드 리뷰 후 Remote premaster branch와 merge작업을 진행한다.
이 과정에서 Remote Repository에 있는 function branch가 삭제된다.



## Contribution, Pull, Branch update

### **Developer**

이제 Developer는 자신의 코드가 merge됐다는 응답을 받았습니다. 드디어 프로젝트에 기여를 하게 되었네요!



이제 Developer는 loginBranch branch에서 더는 작업할 필요가 없습니다. Local환경에서 premaster branch로 이동합니다. 

~~~
git checkout premaster
~~~



Remote premaster branch로부터 pull작업을 진행합니다. 자신의 로컬 환경도 이제 업데이트된 remote와 똑같이 만듭니다.

~~~
git pull origin premaster
~~~

![localFinishmerged](/static/assets/img/blog/usefulSkills/gitlabImages/localFinishmerged.png){: width="100%" height="100%"}



그리고 이제 Local환경에서 loginBranch branch를 삭제해주어야겠죠.

![deleteloginBranch](/static/assets/img/blog/usefulSkills/gitlabImages/deleteloginBranch.png){: width="100%" height="100%"}



이제 branch상황을 보겠습니다. Local에는 master branch와 premaster branch밖에 안남았네요. 대신 remote branch에서 loginBranch branch가 보입니다. GitLab사이트에서만 지웠기 때문에 Local 환경에서는 동기화가 되지 않았습니다. 

이제 `git remote update`와 `git fetch -p`로 동기화를 해줍시다. 

![deleteRemoteWB](/static/assets/img/blog/usefulSkills/gitlabImages/deleteRemoteWB.png){: width="100%" height="100%"}

remote/origin/loginBranch가 삭제된 것을 확인할 수 있습니다. 



### 이제까지의 정리...

Developer는 merge가 완료됐다는 응답을 받으면

Local premaster branch로 이동(git checkout premaster)

Remote premaster branch로부터 pull작업 (git pull origin premaster)

Local working branch를 삭제한다. (git branch -d function)

Remote branch를 update한다. (git remote update, git fetch -p)



## 다시 작업을 시작합니다(프로젝트가 끝날때까지....)

### Developer, Project Manager

Working branch를 하나 만들고(git checkout -b function)
작업 시작.
.
add, commit

conflict확인, merge

add, commit, push

merge request

.

merge

branch delete, branch update

. 

이 과정을 프로젝트가 끝날 때까지 반복합니다!



## The End

### Project Manager

프로젝트가 완성이 되면 PM은 Remote premaster branch에 있는 내용들을 master branch와 merge합니다. 