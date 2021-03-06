# Slack 봇을 이용한 Cherish MVP
`작성자` : [Cherish TI 김소령](https://soryeongk.github.io/)

Cherish 어플 릴리즈 전 MVP 테스트 가능여부 체크를 위한 코드

commit message convention copied from [Cherish-iOS](https://github.com/TeamCherish/Cherish-iOS)

```
- feat    : 기능 (새로운 기능)
- fix     : 버그 (버그 수정)
- refactor: 리팩토링
- style   : 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없음)
- docs    : 문서 (문서 추가, 수정, 삭제)
- test    : 테스트 (테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없음)
- chore   : 기타 변경사항 (빌드 스크립트 수정 등)
```



# Description

소중한 사람들과의 연락을 꾸준히 이어가게 하는 어플 Cherish.

꾸준하게 연락하고 싶은 사람을 주기와 함께 등록하면, 해당 주기에 맞춰서 알림과 함께 연락 수단 연결

즉, 가장 중요한 기능은 **사용자가 설정한 주기에 맞춰서 연락 알림을 주는 것**

# MVP 구현 목표

`날짜` : 2월 7일 일요일

`목표`

- [x] MVP 사용자는 slack 워크 스페이스에 입장.
- [x] 연락하고 싶은 사람의 이름(혹은 애칭)과 연락 주기(n일에 한 번), 알람 시간을 받아서 사람이 수기로 입력
- [ ] 신청 폼 자동화
- [x] 주기에 맞춰서 해당 채팅방에 `남쿵둥이`에게 물을 줄 시간이에요! 라는 메세지 보내주기.
- [x] 일방적으로 메세지만 보내는 것으로 1차 구현
- [ ] `AWS 가상 머신`에 cron으로 연락 주기를 입력하고 그에 맞추어 코드 실행하기
- [ ] `python`을 기본으로 사용하며, 목표 기한 동안은 `1일 1커밋`을 목표로 한다~!

# 얻고자 하는 것

1. 알림을 받는 것만으로 연락에 대한 동기부여가 될까?
2. 얼마나 많은 사람들이 관심을 보일까?
3. 사용자는 어떤 주기로 몇 명의 사람들을 등록할까? - 고민
4. 사용자 중 우리 기능을 n회 이상 사용하는 비율은 어떨까?
5. 릴리즈를 위한 고객 확보!

# 구현 방법
1. MVP 참여자들로부터 `애칭` `연락 주기` `알람 시간`을 받는다.

2. 슬랙 API에서 해당 봇에 맞는 token을 받아 `secret.py`에 저장한다.
   token은 `xoxb-`로 시작하는 문자열이며, `secret.py`는 `.gitignore`에 포함시켜 github에 올라가지 않도록 한다.
   **(github을 비롯한 각종 플랫폼에 공유될 경우 슬랙 API 차단됨)**

3. `slacker`의 `chat.post_message(#channel_name, msg)`를 통해 `#mvp_test`에 `msg`를 보내는 코드를 작성하여 각각의 파일을 만든다. -> `main.py` 참고

4. `crontab -e`으로 크론을 작성한다.

   ```
   형식 : * * * * * [command || .sh]
   각 *은 분, 시간, 일, 요일을 의미
   시간 지정의 경우 인스턴스 환경의 기준시각을 확인(cmd : date, KST : 한국, UCT : 영국)
   기준 시각 변경 명령은 sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
   ```

5. 크론의 command 작성 시 실행 파일(`python3` 등)의 경로를 함께 기재해야할 수도 있다.
   `.sh`로 작성 시에는 `chmod`를 통해 권한 설정을 해야 한다.

   ````
   Cherish mvp cmd : `python3 [route/file_name]
   ````

6. 크론 로그를 남기고 싶은 경우 크론 커멘드 뒤에 `>> [route/log_file_name.log] 2>&1`를 추가하고, `mvp_cron.log`를 경로에 맞추서 생성한 뒤 `chmod 777 [file_name]`을 통해 권한을 설정해준다.
