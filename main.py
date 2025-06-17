import streamlit as st

# 가상의 노래 데이터
SONG_DATA = {
    "Shape of You": {
        "artist": "Ed Sheeran",
        "album": "Divide",
        "release_date": "2017-01-06",
        "lyrics": """The club isn't the best place to find a lover
So the bar is where I go..."""
    },
    "Dynamite": {
        "artist": "BTS",
        "album": "Dynamite",
        "release_date": "2020-08-21",
        "lyrics": """'Cause I, I, I'm in the stars tonight
So watch me bring the fire and set the night alight..."""
    },
    # 필요한 만큼 더 추가 가능
}

def main():
    st.title("🎵 노래 정보 검색")
    st.write("노래 제목을 입력하면 앨범, 가수, 발매일, 가사를 보여줍니다.")

    song_query = st.text_input("노래 제목 입력", "")

    if song_query:
        # 입력받은 노래 제목으로 대소문자 구분 없이 검색
        song_info = None
        for title, info in SONG_DATA.items():
            if title.lower() == song_query.lower():
                song_info = info
                song_title = title
                break

        if song_info:
            st.subheader(f"노래 제목: {song_title}")
            st.markdown(f"**가수:** {song_info['artist']}")
            st.markdown(f"**앨범:** {song_info['album']}")
            st.markdown(f"**발매일:** {song_info['release_date']}")
            st.markdown("**가사:**")
            st.text(song_info['lyrics'])
        else:
            st.warning("해당 노래 정보를 찾을 수 없습니다. 정확한 제목을 입력해 주세요.")

if __name__ == "__main__":
    main()
