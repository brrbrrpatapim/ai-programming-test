
import pandas as pd


# 1. 데이터 정제
def 정제(df):
    print("시작", len(df))

    df = df.dropna(subset=["점수"])
    print("빈 칸 제거", len(df))

    df = df.drop_duplicates().copy()
    print("중복 제거", len(df))

    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()

    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거", len(df))

    return df


# 2. 반별 평균 함수
def 반별평균(df):
    return df.groupby("반")["점수"].mean()


if __name__ == "__main__":
    df = pd.read_csv("scores_2026.csv")
    df = 정제(df)

    print("\n[정제 확인]")
    print(sorted(df["반"].unique()))
    print(sorted(df["과목"].unique()))

    # 3. 필터링
    print("\n[필터링]")
    수학 = df[df["과목"] == "수학"]
    print("수학 행 수:", len(수학))

    # 4. 그룹화
    print("\n[반별 평균]")
    print(반별평균(df))

    print("\n[과목별 반 평균]")
    print(df.groupby(["과목", "반"])["점수"].mean())

    # 5. 통계
    print("\n[반별 통계]")
    print(df.groupby("반")["점수"].agg(
        ["count", "mean", "median", "max"]
    ).round(2))

    # 6. 합계 검증
    print("\n[합계 일치 확인]")
    print("그룹 합계:", df.groupby("반")["점수"].sum().sum())
    print("전체 합계:", df["점수"].sum())

    # 7. 개수 검증
    print("\n[개수 일치 확인]")
    print("그룹 개수:", df.groupby("반")["점수"].count().sum())
    print("전체 개수:", len(df))

    # 8. 스팟 체크
    print("\n[1반 수학 점수]")
    print(df[(df["반"] == "1반") &
             (df["과목"] == "수학")]["점수"])
