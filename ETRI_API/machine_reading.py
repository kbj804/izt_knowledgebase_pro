
#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"
accessKey = "aac4fba1-db31-4078-96d9-f21671d9ed9b"

question = "igate가 뭐야?"


passage1 = "[메이플스토리 탈퇴 방법] ① 메이플스토리 홈페이지 로그인 후 로그인 정보 아래 마이메이플을 클릭합니다. ② 로그인 메뉴 하단에 확인되는 마이메이플 메뉴 아래 메이플ID 탈퇴신청을 클릭합니다. ③ 휴대폰 or 신용/체크카드 or 마이핀을 통한 본인인증 후 탈퇴할 수 있어요."
passage2 = "이미 탈퇴가 완료되었다면 되돌릴 수 없지만 탈퇴한 당일! [메이플스토리 탈퇴 취소 방법] 1) 탈퇴한 메이플ID가 연결되었던 넥슨ID의 다른 메이플ID로 로그인해야 합니다. 2) 매일 오전 4시를 기준으로 메이플ID가 완전히 삭제되기 때문에 오전 4시 이후에는 탈퇴 취소할 수 없습니다. 3) 넥슨ID에 연동된 모든 메이플ID를 탈퇴했다면 탈퇴 취소가 불가능합니다."
#passage = passage1 + passage2 +passage3 + passage4 +passage5 + passage6 + passage7 + passage8
passage3 = "본 장에서는 iGate에 대한 기본적인 이해와 iGate의 개념과 아키텍처를 기술한다. 다양한 채널과 서비스를 통합하는 인프라 구축을 통해 업무시스템이 채널로부터 독립적일 수 있게 보장하며, 일관성 있는 정보 제공으로 IT 비즈니스의 효율성을 극대화한다. iGate 4.0 는 SOA(Service-Oriented Architecture)기반의 ESB 엔진을 근간으로 하고 있으며, 대/내외의 채널별 공통 업무와 채널 고유 업무를 효율적으로 처리하는 중요 영역과 Application 의 인터페이스 표준화를 지원함으로써 Middle Layer Integration 의 실현을 위해 다음과 같은 사상을 기본으로 하는 솔루션이다. 기존의 각 어플리케이션들은 멀티채널 통합 아키텍처 상에서 통합되어야 한다. 코어의 어플리케이션들은 SOA 상에서 데이터 로직을 제공하는 서비스 프로바이더로 존재하고, 비즈니스 프로세스는 멀티채널 통합 layer에 구현된다. 이러한 비즈니스 프로세스는 각 채널에서 재사용, 공유하여야 한다. "
passage = passage1 + passage2 + passage3

requestJson = {
"access_key": accessKey,
    "argument": {
        "question": question,
        "passage": passage
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))
                                     