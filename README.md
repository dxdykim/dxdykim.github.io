# Dohyeon Kim — Academic Website

Homepage: https://dxdykim.github.io/

최신 CV에 맞춰 업데이트한 개인 학술 홈페이지입니다. 기존 Academic Pages/Jekyll 구조를 유지하면서 메인 페이지를 간결한 HTML/CSS 디자인으로 바꾸었습니다.

## 내용 수정

| 파일 | 내용 |
| --- | --- |
| `_pages/about.html` | 소개, 논문, 발표·방문, 강의·멘토링, 학력·봉사 활동 |
| `assets/style.css` | 메인 페이지의 색상·글꼴·간격·모바일 배치 |
| `assets/portrait.webp` | 프로필 사진 |
| `_pages/cv.md` | 기존 공개 CV 페이지로 연결 |

GitHub에서 해당 파일을 열고 연필 버튼으로 수정한 뒤 Commit changes를 누르면 홈페이지가 갱신됩니다. 현재 CV 링크는 기존 공개 홈페이지의 CV 페이지로 연결됩니다. 새 CV를 공개한 뒤에는 `_pages/about.html`의 CV 링크와 `_pages/cv.md`의 `redirect_to`를 함께 수정합니다.

논문을 추가하려면 `PUBLICATIONS` 주석 아래의 `<li>…</li>`를 복사하고 제목·저자·상태·링크를 함께 바꿉니다. CSS의 `counter-reset: papers 7` 값은 논문 수 + 1로 유지합니다. 예정된 일정은 `EVENTS` 주석 아래에서 관리하고, 페이지 맨 아래 업데이트 날짜도 함께 수정하세요.

## 배포 구조

- 기존 `master` 브랜치와 GitHub Pages/Jekyll 배포를 사용합니다.
- `_pages/about.html`의 `permalink: /`가 홈페이지 주소를 지정합니다. `layout: null`이 있어야 새 페이지에 이전 테마가 중복 적용되지 않습니다.
- 기존 문서·논문·발표 상세 페이지의 소스와 파일은 보존되어 있습니다.
- `.nojekyll`은 추가하지 마세요. 기존 상세 페이지의 생성에 Jekyll이 필요합니다.
- `www.doh-yeon-kim.com`의 DNS와 Owlstown 연결은 변경하지 않았습니다.

홈페이지 내용은 제공된 최신 CV를 바탕으로 업데이트했습니다. 첨부 PDF 원본은 이 저장소에 업로드하지 않았습니다. 사진·Google Scholar 링크·학부 소개는 기존 개인 홈페이지에서 가져왔습니다. 새 디자인은 Lin Lin, Simran Arora, Sinho Chewi의 학술 홈페이지 구성을 참고해 작성했습니다. 이전 테마의 라이선스와 관련 소스는 그대로 남아 있습니다.
