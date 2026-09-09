# Dohyeon Kim — Academic Website

Homepage: https://dxdykim.github.io/

최신 CV에 맞춰 업데이트한 개인 학술 홈페이지입니다. 기존 Academic Pages/Jekyll 구조를 유지하면서 메인 페이지를 간결한 HTML/CSS 디자인으로 바꾸었습니다.

## 내용 수정

| 파일 | 내용 |
| --- | --- |
| `_pages/about.html` | 소개, 논문, 발표·방문, 강의·멘토링, 학력·봉사 활동 |
| `assets/style.css` | 메인 페이지의 색상·글꼴·간격·모바일 배치 |
| `assets/portrait.webp` | 프로필 사진 |
| `assets/CV_Dohyeon_Kim.pdf` | 최신 CV PDF |
| `assets/slides/siam-uq-2026.pdf` | SIAM UQ 2026 발표 슬라이드 |
| `assets/teaching/acm270-lecture1.pdf` | ACM 270 Lecture 1 강의록 (Draft — under revision) |
| `assets/teaching/acm270-lecture2.pdf` | ACM 270 Lecture 2 강의록 (Draft — under revision) |
| `_pages/cv.md` | CV PDF로 연결하는 기존 `/cv/` 경로 |
| `_pages/others.html` | Others: 세 개의 개인 소개 글 목록 |
| `_pages/books.html` | Books I Live With: 독서 이야기와 2024·2025년 독서 목록 |
| `_pages/math-path.html` | A Nonlinear Path to Mathematics: 경영학에서 수학으로 옮겨온 과정 |
| `_pages/squat-think-repeat.html` | Squat, Think, Repeat: 운동 이야기 |
| `_layouts/personal.html` | Others 목록과 개별 글의 공통 레이아웃 |

GitHub에서 해당 파일을 열고 연필 버튼으로 수정한 뒤 Commit changes를 누르면 홈페이지가 갱신됩니다. CV·슬라이드·강의록을 같은 경로와 파일명으로 교체하면 기존 링크가 새 파일로 연결됩니다. 홈페이지 본문의 내용과 원고 상태는 `_pages/about.html`에서도 따로 수정해야 합니다.

논문을 추가하려면 `PUBLICATIONS` 주석 아래의 `<li>…</li>`를 복사하고 제목·저자·상태·링크를 함께 바꿉니다. CSS의 `counter-reset: papers 7` 값은 논문 수 + 1로 유지합니다. 예정된 일정은 `EVENTS` 주석 아래에서 관리하고, 페이지 맨 아래 업데이트 날짜도 함께 수정하세요.

## 방문 통계 (GoatCounter)

방문 추이, 페이지별 조회, 유입 경로 등을 GoatCounter에서 확인할 수 있도록 연결 코드를 준비했습니다. `_config.yml`의 `analytics.goatcounter.code`가 비어 있는 동안에는 분석 스크립트를 불러오지 않으며, 방문 집계도 시작되지 않습니다.

### 처음 연결하기

1. [GoatCounter 가입 페이지](https://www.goatcounter.com/signup)에서 계정을 만듭니다. Account name은 원하는 이름을 선택하고, Site domain에는 `www.doh-yeon-kim.com`을 입력합니다. [이용약관](https://www.goatcounter.com/help/terms)에 따라 최초 가입은 본인이 직접 해야 합니다.
2. GoatCounter의 **Settings → Site settings → Dashboard viewable by**를 **Only logged in users**로 둡니다. **Allow adding visitor counts on your website**도 체크하지 않습니다.
3. GitHub에서 `_config.yml`을 열고 `analytics` 아래 `goatcounter`의 `code: ""`에 가입 시 정한 Account name만 입력합니다. 전체 주소나 `/count`를 넣지 않습니다. 비밀번호나 API 토큰은 필요하지 않습니다.
4. Commit changes 후 GitHub Pages 배포가 끝나면 집계가 시작됩니다. 가입한 `https://계정이름.goatcounter.com`에서 로그인해 통계를 봅니다. 홈페이지에는 방문자 수나 통계 링크가 표시되지 않습니다.

첫 화면과 Others 페이지, 기존 Jekyll 상세 페이지에 같은 설정이 적용됩니다. 개발 환경에서는 집계하지 않습니다. 페이지 통계는 URL 경로별로 묶습니다. PDF를 직접 여는 방문에는 이 스크립트가 실행되지 않습니다.

### 내 방문 제외하기

연결 후 사용하는 브라우저에서 `https://www.doh-yeon-kim.com/#toggle-goatcounter`를 열고 팝업에서 이 브라우저의 집계가 비활성화되었는지 확인합니다. 주소만 수정해서 팝업이 나타나지 않았을 때만 새로고침합니다. 다른 브라우저나 기기에서는 각각 설정해야 하며, 같은 링크를 다시 실행하면 설정이 반대로 전환됩니다. [공식 안내](https://www.goatcounter.com/help/skip-dev)

### 나중에 통계 공개하기

공개하기로 결정하면 GoatCounter에서 **Dashboard viewable by → Anyone**으로 바꿀 수 있습니다. 홈페이지에 방문자 수를 표시하는 기능은 별도로 켜야 합니다. 현재는 비공개 대시보드를 전제로 하며, 통계 데이터나 로그인 정보는 GitHub 저장소에 저장하지 않습니다.

집계를 중지하려면 `_config.yml`의 `analytics.provider`를 `false`로 바꾸고 배포합니다. 이전에 쌓인 통계의 공개 여부와 삭제는 GoatCounter에서 관리합니다.

## 배포 구조

- 기존 `master` 브랜치와 GitHub Pages/Jekyll 배포를 사용합니다.
- `_pages/about.html`의 `permalink: /`가 홈페이지 주소를 지정합니다. `layout: null`이 있어야 새 페이지에 이전 테마가 중복 적용되지 않습니다.
- 기존 문서·논문·발표 상세 페이지의 소스와 파일은 보존되어 있습니다.
- `.nojekyll`은 추가하지 마세요. 기존 상세 페이지의 생성에 Jekyll이 필요합니다.
- `www.doh-yeon-kim.com`의 DNS와 Owlstown 연결은 변경하지 않았습니다.

홈페이지 내용은 제공된 최신 CV와 본인의 수정 요청을 반영했습니다. CV·SIAM UQ 슬라이드·ACM 270 강의록 두 개는 공개 게시가 승인된 원본 파일입니다. 홈페이지의 ACM 270 날짜는 실제 강의일인 2026년 4월 28일과 30일이며, PDF 표지 날짜와는 다릅니다. 사진·Google Scholar 링크·학부 소개는 기존 개인 홈페이지에서 가져왔습니다. 새 디자인은 Lin Lin, Simran Arora, Sinho Chewi의 학술 홈페이지 구성을 참고해 작성했습니다. 이전 테마의 라이선스와 관련 소스는 그대로 남아 있습니다.
