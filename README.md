# 결(Gyeol) — 마음을 노래로

글 한 편이 노래가 되는 AI 작사·작곡 서비스 MVP.

사용자가 편지·일기·시·메모 등 **아무 글이나 붙여넣으면**, AI가 그 글의 분위기·감정·서사를 읽어  
원하는 장르로 **작사 + 음악 생성 프롬프트**까지 완성해 드립니다.

## 핵심 차별점 (이번 버전 반영)

1. **한글 가사 ↔ 곡 어울림 강화**  
   - 음절 수 일관성, 발음 용이성, 강세·운율 최적화  
   - “보컬 친화형” 가사 안을 기본 제공 (AI 보컬이 한국어를 잘 못 불러도 멜로디와 자연스럽게 맞물리도록)

2. **악기 다양성 + 고음질**  
   - 장르별 4~6개 레이어드 악기 편성  
   - high-fidelity, clean mix, professional mastering 지시 기본 포함

3. **창작 기여 리포트**  
   - 원문 + 선택·수정 이력을 기록 → 저작권/KOMCA 대응용

## 빠른 시작

```bash
cd gyeol-music
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# .env 파일 생성
echo "XAI_API_KEY=xai-..." > .env

streamlit run app.py
```

## 사용 흐름

1. 글 입력 (예시 제공)
2. 감정 해석 카드 + 추천 장르 3안
3. 음악 디렉션 확인 (악기·BPM·보컬)
4. 가사 3안 비교 → 보컬 친화형 선택 가능
5. Suno/Udio/ElevenLabs 등에 바로 붙여넣을 수 있는 **완성 프롬프트** + 가사 + 창작 기여 리포트 다운로드

## 환경 변수

| 변수 | 설명 |
|------|------|
| `XAI_API_KEY` | xAI Grok API 키 (필수) |
| `XAI_BASE_URL` | 기본 `https://api.x.ai/v1` |

## 기술 스택

- Streamlit
- xAI Grok (구조화 JSON 출력)
- Pydantic / ReportLab (향후 PDF 확장)

## 라이선스 / 주의

- AI 생성물임을 명시합니다.
- 사용자의 원문과 선택·수정이 창작 기여의 핵심입니다.
- 상업적 음원 발매는 벤더 약관과 국내 규제를 별도 확인하세요.

---

**결(結)** — 마음을 노래로.
