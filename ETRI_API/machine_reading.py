
#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"
accessKey = "aac4fba1-db31-4078-96d9-f21671d9ed9b"

question = "인젠트가 뭐했어?"


#passage1 = "[메이플스토리 탈퇴 방법] ① 메이플스토리 홈페이지 로그인 후 로그인 정보 아래 마이메이플을 클릭합니다. ② 로그인 메뉴 하단에 확인되는 마이메이플 메뉴 아래 메이플ID 탈퇴신청을 클릭합니다. ③ 휴대폰 or 신용/체크카드 or 마이핀을 통한 본인인증 후 탈퇴할 수 있어요."
#passage2 = "이미 탈퇴가 완료되었다면 되돌릴 수 없지만 탈퇴한 당일! [메이플스토리 탈퇴 취소 방법] 1) 탈퇴한 메이플ID가 연결되었던 넥슨ID의 다른 메이플ID로 로그인해야 합니다. 2) 매일 오전 4시를 기준으로 메이플ID가 완전히 삭제되기 때문에 오전 4시 이후에는 탈퇴 취소할 수 없습니다. 3) 넥슨ID에 연동된 모든 메이플ID를 탈퇴했다면 탈퇴 취소가 불가능합니다."
#passage = passage1 + passage2 +passage3 + passage4 +passage5 + passage6 + passage7 + passage8
#passage3 = "본 장에서는 iGate에 대한 기본적인 이해와 iGate의 개념과 아키텍처를 기술한다. 다양한 채널과 서비스를 통합하는 인프라 구축을 통해 업무시스템이 채널로부터 독립적일 수 있게 보장하며, 일관성 있는 정보 제공으로 IT 비즈니스의 효율성을 극대화한다. iGate 4.0 는 SOA(Service-Oriented Architecture)기반의 ESB 엔진을 근간으로 하고 있으며, 대/내외의 채널별 공통 업무와 채널 고유 업무를 효율적으로 처리하는 중요 영역과 Application 의 인터페이스 표준화를 지원함으로써 Middle Layer Integration 의 실현을 위해 다음과 같은 사상을 기본으로 하는 솔루션이다. 기존의 각 어플리케이션들은 멀티채널 통합 아키텍처 상에서 통합되어야 한다. 코어의 어플리케이션들은 SOA 상에서 데이터 로직을 제공하는 서비스 프로바이더로 존재하고, 비즈니스 프로세스는 멀티채널 통합 layer에 구현된다. 이러한 비즈니스 프로세스는 각 채널에서 재사용, 공유하여야 한다. "
passage = "인젠트(대표 정성기)는 SSG닷컴에 '엑스퍼디비(eXperDB)' 플랫폼을 활용한 퍼블릭클라우드와 온프레미스 장점을 결합한 하이브리드클라우드를 구축했다고 3일 밝혔다. 인젠트는 국내 금융권 채널통합시스템 점유율 1위 솔루션 기업으로 최근 오픈소스DBMS 기반 통합 데이터플랫폼 영역까지 사업을 확대했다. 인젠트는 기존 SSG닷컴의 온프레미스 형태 업무시스템을 유지하며 특정기간내 대량 트래픽이 발생하는 온라인 이벤트 진행시 효율적 DBMS 서비스 대응을 목표로 이번 프로젝트를 시작했다. 인젠트는 최소 비용과 리소스를 활용해 온프레미스에 구축된 업무 데이터를 엑스퍼디비 복제기능으로 온프레미스와 퍼블릭클라우드간 거래 안정성과 데이터 정합성을 유지한다. 이벤트 중 발생하는 대량 트래픽 수용을 위한 자동 확장 기능을 퍼블릭클라우드존에 적용했다. " 

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
                                     