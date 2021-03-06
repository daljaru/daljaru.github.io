---
layout: post
title: "SoftwareDocuments"
date: 2020-05-25
desc: "How to write Software Project documents??"
keywords: 설계, 요구사항, 분석, 작업, 진행
categories: [Useful]
tags: [Software, Architecture, Documents]
---

**소프트웨어 설계보고서를 보다 잘 작성하는 방법을 적었습니다.** 설계보고서 작성방법과 관련한 내용을 찾으실 때 도움이 되었으면 좋겠습니다.
<br>
<br>

# 소프트웨어 설계란?
___
소프트웨어 설계(Software design)란 소프트웨어 해결책을 위한 **문제해결**과 **계획 과정**입니다. 소프트웨어의 목적과 명세가 결정되면 개발자가 설계 하거나 설계자를 고용하여 해결책을 위한 계획을 개발하도록 합니다. 저수준 요소와 알고리즘 구현 문제, 그리고 구조에 대한 조망이 포함됩니다.   -by wikipedia
<br>
<br>

## 1. 소프트웨어 설계과제의 문제를 정의한다.
___
* 프로젝트의 주제 정리.
* 프로젝트의 목적을 정의, 설명.
* 설계하려는 대상을 명확히 제시. 
* 해결하려는 문제가 무엇인지 명시.
<br>
<br>

## 2. 요구사항을 분석한다. 
___
#### 소프트웨어의 요구사항을 분석하는 기준은 크게 두가지입니다. 

1. **기능요구조건** - 설계과제의 문제를 정의하고 해당 문제를 해결하기 위해 필요한 기능을 나열합니다. 
   
2. **성능규격조건** - 프로젝트의 목적(목표)를 정량적인 항목으로 나타냅니다. (수치화) 정량적인 표현이 어려울 경우에는 정성적인 표현을 적으시면 됩니다. 
<br>
<br>

## 3. 제한요소를 분석한다. 
___
소프트웨어를 만들 때 가장 중요한 것은 **효율성**이죠. 효율성을 최대로 내려면 어떤 조건들을 고려해야 할까요. 소프트웨어가 동작하는 환경, 개발환경, 비용, 사회성, 시장성 등을 고려해야할 것입니다. 엄청난 부자가 아닌이상 제한된 자원을 투자해서 소프트웨어를 설계해야하니까요.

1. **동작환경** - 소프트웨어가 동작하는 환경을 고려합니다. 고려사항 중에 분석한 요구사항을 만족시키지 못하는 부분이 있다면 이를 고려해야하고 대안선택에 영향을 주는 부분들을 고려하여 기술해야합니다.
   
2. **개발환경** - 분석한 요구사항을 만족시키기 위한 개발도구를 선택함에 있어 제한을 주는 요소들을 기술합니다. 개발 도구의 접근성, 사용편의성, 개발자의 숙련도 등을 파악합니다.
   
3. **개발비용** - 요구사항을 모두 만족시키기 위한 비용범위를 기술합니다. 
   
4. **사회성** - 사회성이라는 말에는 다양한 의미가 함축되어 있습니다. 사회적/ 윤리적/ 법률적 제한요소들을 분석하여 기술합니다.
   
5. **시장성** - 소프트웨어를 판매를 해야 할 경우 사회적으로 수요가 많은지 판단을 해야합니다. 
<br>
<br>

## 4. 설계안을 도출합니다. 
___
1. **설계목표를 정의**합니다. - 설계 목표는 설계 명세와 제약 조건을 만족하는 결과물을 만들어 내기 위하여 정해야 합니다. 설계목표를 설정하는 방법으로 [목적나무](http://www.managingforimpact.org/tool/objective-tree)를 이용하는 방법이 있습니다. 설계의 단위 목적들을 체계적으로 정리할 수 있습니다.
   
2. **설계안을 작성**합니다. - 설계한 내용을 구체적인 설계안을 통하여 제시합니다. 설계안을 효과적으로 제시하는 방법에는 [블록도](https://www.smartdraw.com/block-diagram/)를 이용하는 방법이 있습니다. 기능별로 접근방안들을 제시할 수 있습니다. 물론 다양한 설계안을 도출하는 것이 좋습니다. 또한 다각적인 검토와 평가를 통해 최종 설계안을 결정하는 과정을 보여주는 것도 좋습니다. 필요시 결과물 제작을 위한 설계도를 상세히 명시합니다. 
   
3. **평가 항목과 평가 방법** - 결과물이 제작된다면 이를 평가할 수 있는 항목과 각 항목에 대한 평가 방법을 기술합니다. 평가항목들은 수치로 나타내는 것이 좋습니다. 수치로 나타낼 수 없는 경우가 있을 수 있습니다. 이는 성능수준을 규정하는데 한계가 있습니다.
   
4. **대안을 분석**합니다. - 제시된 설계안과 기존 방안을 3)에서 제시한 평가항목의 결과를 통해 비교, 분석하여 제시된 설계안이 우수한 것이라는 것을 입증합니다. 
<br>
<br>

## 5. 구현
___
1. **구현방법** - 결과물의 시스템 상세 구조를 제시하고 각각의 요소에 대해 구현 방법을 설명합니다. 블록다이어그램을 사용하는 것이 좋습니다. 각 단위블록에서 어떤 구현방법이 있는지 설명할 수 있으면 좋습니다. 이때 수학과 기초과학 이론을 응용했다면 이에 대한 이론도 자세하게 기술합니다.
   
2. **구현 도구** - 구현에 사용한 도구들과 기술, 상세 부품목록 등을 기술합니다.<br>개발툴, 특정 시스템이나 플랫폼을 사용하였다면 그 시스템이나 플랫폼의 특징 및 내재된 기능에 대해서도 기술합니다.
<br>
<br>

## 6. 결과
___
1. **결과물 설명** - 구현을 통해 얻은 결과물을 기술합니다. 결과물에 대한 사진이나 기타 시각 효과를 낼 수 있는 그림을 첨부합니다.
   
2. **결과물 분석** - 결과물을 4-3)에서 제시한 평가항목과 평가방법에 맞추어 평가하고 결과를 분석합니다.
<br>
<br>

## 7. 작업진행 방법
___
1. **작업 분담 구조** - 전체 업무를 팀원끼리 어떻게 배분하여 수행했는지를 기술합니다. 팀원 개개인의 역할과 책임이 명확하게 구분되어 있어야 합니다.
   
2. **설계 일정 및 역할 분담** - 전체 프로젝트 업무를 진행된 일정과 함께 기술합니다. 대표적인 기술방법으로 Gantt Chart가 있습니다.
   
3. **예산 집행 내역** - 구현에 사용된 부품 목록에 따른 재료비를 포함하여 예산이 어떻게 사용되었는지를 기술합니다.
<br>
<br>

## 8. 결론
___
1. **결론** - 진행 배경, 문제 정의, 설계, 결과물 구현 등 프로젝트의 전반적 사항들을 잘 정리하여 간단히 요약하고 그 과정들을 통하여 도출된 결론을 기술합니다. 이때 프로젝트를 통해 만들어진 결과물이 요구사항 및 제한 조건들을 모두 만족시키는지에 대해서도 함께 설명합니다. 프로젝트 주제와 관련하여 배운 점을 다양한 측면에서 기술하며 프로젝트 목표의 달성여부를 명확하게 표현합니다.
   
2. **결과 분석** - 최종 결과물의 핵심요소를 요약하고, 결과물의 장단점을 분석합니다. 프로젝트 결과가 경제적, 사회적, 윤리적, 환경 및 안전성의 관점에서 미칠 파급효과에 대하여 상세히 기술합니다.
<br>
<br>

## 9. 참고문헌
___
 프로젝트를 진행하고 보고서를 작성하는 데 참고한 자료들을 나열합니다. 참고자료는 모두 본문 내 인용이 필요한 위치에서 출처를 분명히 밝혀야 하며, 양식에 의거하여 작성하여야 합니다. 문서 자료 외에도 다양한 자료들을 포함시킬 수 있습니다.

 **예시**를 들어드리겠습니다. 

[1] 저자, 제목, 출판사, 출판연도

[2] 저자, 제목, 출판사, 개정횟수, chapter이름, pp. 100-101, 출판연도

[3] 검색키워드, 해당페이지 URL(검색날짜: 2019-05-05)