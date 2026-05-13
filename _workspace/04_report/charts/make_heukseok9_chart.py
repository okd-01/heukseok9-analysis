"""흑석 9구역 84㎡(30평대) 매매가 추정 차트 (2026 Q2 ~ 2029 Q4).

- 베이스/상방/하방 3개 시나리오 + 범위 영역
- 마일스톤(분양, 입주) 표시
- 인근 신축 비교 기준 점선
"""
from __future__ import annotations

import os

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False

# 분기 라벨과 인덱스
quarters = [
    "26Q2", "26Q3", "26Q4",
    "27Q1", "27Q2", "27Q3", "27Q4",
    "28Q1", "28Q2", "28Q3", "28Q4",
    "29Q1", "29Q2", "29Q3", "29Q4",
]
x = np.arange(len(quarters))

# 시나리오별 중심값 (억원)
base = np.array([
    25.5, 26.2, 27.0,                      # 2026: 입주권 시세 완만 상승
    27.8, 28.5, 29.5, 30.5,                # 2027: 분양 + 프리미엄 반영
    31.2, 32.0, 32.8, 33.5,                # 2028: 분양권, 입주 임박
    34.2, 35.0, 35.7, 36.5,                # 2029: 입주 임박~입주
])
upper = np.array([
    27.5, 28.5, 29.5,
    30.5, 31.8, 33.0, 34.2,
    35.5, 36.8, 38.0, 39.3,
    40.5, 41.8, 43.0, 44.0,
])
lower = np.array([
    23.0, 23.8, 24.5,
    25.2, 25.8, 26.5, 27.2,
    27.8, 28.3, 28.8, 29.3,
    30.0, 30.5, 31.0, 31.5,
])

fig, ax = plt.subplots(figsize=(12, 7))

# 범위 영역
ax.fill_between(x, lower, upper, color="#9ec6e8", alpha=0.25, label="추정 범위(하방~상방)")

# 라인 3개
ax.plot(x, upper, color="#1f5fa8", linewidth=1.6, linestyle="--", marker="^",
        markersize=5, label="상방 시나리오")
ax.plot(x, base, color="#0f3a8a", linewidth=2.4, marker="o",
        markersize=6, label="베이스 시나리오")
ax.plot(x, lower, color="#7d7d7d", linewidth=1.6, linestyle="--", marker="v",
        markersize=5, label="하방 시나리오")

# 비교 기준 (인근 신축 84㎡)
ax.axhline(y=25.0, color="#c97a00", linewidth=1.2, linestyle=":", alpha=0.9)
ax.text(0.1, 25.35, "인근 신축 84㎡ 참고선 ~ 25억 (아크로리버하임·흑석자이, 2025~2026)",
        color="#c97a00", fontsize=9)

# 마일스톤: 2027 일반분양
idx_sale = quarters.index("27Q2")
ax.axvline(x=idx_sale, color="#cc3333", linewidth=1.2, alpha=0.7)
ax.text(idx_sale + 0.05, lower.min() - 0.8, "2027 일반분양\n(분양가 84㎡ ≈ 20억)",
        color="#cc3333", fontsize=9, va="top")

# 마일스톤: 2029 입주 예상
idx_move = quarters.index("29Q3")
ax.axvline(x=idx_move, color="#2e8b57", linewidth=1.2, alpha=0.7)
ax.text(idx_move + 0.05, lower.min() - 0.8, "2029 H2 입주 예상",
        color="#2e8b57", fontsize=9, va="top")

# 단계 배경 음영
ax.axvspan(-0.5, idx_sale - 0.5, color="#fff7e6", alpha=0.45, zorder=0)
ax.axvspan(idx_sale - 0.5, idx_move - 0.5, color="#eaf3ff", alpha=0.45, zorder=0)
ax.axvspan(idx_move - 0.5, len(x) - 0.5, color="#eafaf1", alpha=0.45, zorder=0)
ax.text(1.0, 43.5, "입주권 거래", fontsize=10, color="#a05a00", alpha=0.8)
ax.text(idx_sale + 0.4, 43.5, "분양권 거래", fontsize=10, color="#1f5fa8", alpha=0.8)
ax.text(idx_move + 0.1, 43.5, "신축 거래", fontsize=10, color="#2e8b57", alpha=0.8)

# 축 설정
ax.set_xticks(x)
ax.set_xticklabels(quarters, rotation=0, fontsize=9)
ax.set_xlim(-0.5, len(x) - 0.5)
ax.set_ylim(20, 46)
ax.set_yticks(np.arange(20, 47, 2))
ax.set_xlabel("분기", fontsize=11)
ax.set_ylabel("매매가 (억원)", fontsize=11)
ax.set_title("흑석 9구역(디에이치 켄트로나인) 30평대(전용 84㎡) 매매가 추정\n"
             "2026 Q2 ~ 2029 Q4 · 시나리오 3종 (베이스/상방/하방)",
             fontsize=13, pad=14)
ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)
ax.legend(loc="upper left", fontsize=9, framealpha=0.92)

# 캡션
caption = ("출처: 국토부 정비사업·언론 보도(서울경제·뉴시티데일리·디벨로퍼뉴스·한국경제), "
           "KB부동산 인근 신축 시세, 한국부동산원 입주물량 전망 · "
           "단위: 억원 (전용 84㎡ 기준) · 작성일: 2026-05-13\n"
           "주의: 미래 추정으로 시장·정책·일정 변수에 따라 실제와 다를 수 있음")
fig.text(0.5, -0.02, caption, ha="center", fontsize=8.5, color="#444444",
         wrap=True)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "heukseok9_84_2026_2029.png")
fig.tight_layout()
fig.savefig(out_path, dpi=160, bbox_inches="tight", facecolor="white")
print("SAVED:", out_path)
