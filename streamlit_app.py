import streamlit as st

# 1. 페이지 설정 (웹 브라우저 탭에 표시될 내용)
st.set_page_config(
    page_title="나의 자기소개 페이지",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 구성 (연락처 및 링크)
with st.sidebar:
    st.header("Contact & Links")
    st.markdown("📧 **Email:** your_email@example.com")
    st.markdown("🐙 **GitHub:** [github.com/your-profile](https://github.com)")
    st.markdown("📝 **Blog:** [my-blog.com](https://google.com)")
    
    st.write("---")
    st.caption("© 2026. 길동 All rights reserved.")

# 3. 메인 화면 구성
# 타이틀 및 한 줄 소개
st.title("안녕하세요! 홍길동입니다 👋")
st.subheader("💡 문제를 해결하는 것을 좋아하는 풀스택 개발자입니다.")

st.write("---")

# 레이아웃 나누기 (왼쪽: 프로필 이미지 대체, 오른쪽: 소개글)
col1, col2 = st.columns([1, 2])

with col1:
    # 이미지가 있다면 주석을 해제하고 경로를 넣으세요.
    # st.image("profile.jpg", width=200)
    
    # 이미지 대신 귀여운 이모지와 텍스트로 프로필 영역 만들기
    st.markdown(
        """
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;">
            <span style="font-size: 50px;">🧑‍💻</span>
            <br><b>홍길동 (Gildong Hong)</b>
            <br><small>Seoul, South Korea</small>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col2:
    st.markdown("### 📝 About Me")
    st.write(
        """
        안녕하세요! 새로운 기술을 배우고 이를 통해 실질적인 가치를 만드는 것에 열정을 가진 개발자입니다. 
        단순히 코드를 짜는 것에 그치지 않고, 사용자의 불편함을 찾아내어 개선하는 과정에서 큰 보람을 느낍니다.
        
        현재는 파이썬 기반의 데이터 분석 및 웹 애플리케이션 개발에 집중하고 있습니다.
        """
    )

st.write("---")

# 4. 기술 스택 (Tech Stacks) 영역
st.markdown("### 🛠 Tech Stacks")

# 여러 개의 탭으로 나누어 기술 스택 보여주기
tab1, tab2, tab3 = st.tabs(["Languages", "Frameworks & Tools", "Soft Skills"])

with tab1:
    st.markdown("- **Python** (Advanced)")
    st.markdown("- **JavaScript** (Intermediate)")
    st.markdown("- **SQL** (Intermediate)")

with tab2:
    st.markdown("- **Streamlit** / FastAPI / Django")
    st.markdown("- **Git & GitHub** (Version Control)")
    st.markdown("- **Docker** (Basic)")

with tab3:
    st.markdown("- 🔍 **문제 해결 능력:** 복잡한 에러의 원인을 끝까지 추적하고 해결합니다.")
    st.markdown("- 🗣 **원활한 소통:** 개발 지식이 없는 직군과도 이해하기 쉬운 언어로 소통합니다.")

st.write("---")

# 5. 프로젝트 경험이나 경력 요약
st.markdown("### 🚀 Projects")

# Streamlit의 Expander(접기/펼치기) 기능 활용
with st.expander("1. 스트림릿 기반 자기소개 웹 포트폴리오 제작"):
    st.write("**기간:** 2026.05 - 2026.06")
    st.write("**설명:** 파이썬 스트림릿 프레임워크를 활용하여 나만의 이력서와 포트폴리오를 웹상에 빠르게 띄우는 프로젝트를 진행했습니다.")
    st.write("**사용한 기술:** Python, Streamlit, HTML/CSS")

with st.expander("2. 데이터 시각화 대시보드 구축"):
    st.write("**기간:** 2025.11 - 2026.02")
    st.write("**설명:** 공공 데이터를 활용하여 지역별 트렌드를 한눈에 볼 수 있는 인터랙티브 대시보드를 개발했습니다.")
    st.write("**사용한 기술:** Python, Pandas, Plotly")

st.write("---")

# 6. 방문자 한마디 (간이 방명록 기능)
st.markdown("### 💬 방명록")
visitor_name = st.text_input("이름을 입력해주세요:", placeholder="홍길동")
visitor_message = st.text_area("응원의 한마디를 남겨주세요!", placeholder="내용을 입력하세요.")

if st.button("남기기"):
    if visitor_name and visitor_message:
        st.success(f"🎉 {visitor_name}님의 메시지가 등록되었습니다! (감사합니다!)")
        # 실제 데이터베이스에 저장하는 코드를 여기에 추가할 수 있습니다.
        st.info(f"**[{visitor_name}]**: {visitor_message}")
    else:
        st.warning("이름과 메시지를 모두 입력해주세요!")