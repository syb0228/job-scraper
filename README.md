# job-scraper

- **채용 정보 회사 스크랩** 
  - 회사명, 회사 사이트 주소
  
- **각 회사에 대한 일자리 정보 스크랩** 
  - 지역, 지점명, 알바 시간, 시급, 업로드 시간
  
- 회사별로 스크랩한 알바 정보를 각각 csv. 파일로 만들어서 저장 
  - 파일명은 회사명 사용
  
- 코드의 재사용성을 높이기 위해 보일러 플레이트를 이용
  - 스크랩이 필요한 채용 사이트를 추가할 때마다 발생하는 코드 변경 횟수를 최소화할 수 있음
  
- 반복 검색 속도를 높이기 위해 fakeDB 구현