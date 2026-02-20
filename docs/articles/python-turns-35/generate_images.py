"""Generate beautiful, modern PNG images for the Python Turns 35 articles."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
import os

output_dir = os.path.dirname(os.path.abspath(__file__)) + "/images"
os.makedirs(output_dir, exist_ok=True)


def featured_image():
    """Create a modern, abstract featured image for Python at 35."""
    fig, ax = plt.subplots(figsize=(10.24, 7.68), dpi=100)

    # Dark gradient background
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack([gradient] * 256)
    ax.imshow(gradient, aspect='auto', cmap='viridis',
              extent=[0, 10.24, 0, 7.68], alpha=0.3)
    ax.set_facecolor('#0d1117')
    fig.set_facecolor('#0d1117')

    # Floating circles (abstract nodes)
    np.random.seed(35)
    for _ in range(40):
        x = np.random.uniform(0.5, 9.7)
        y = np.random.uniform(0.5, 7.2)
        r = np.random.uniform(0.05, 0.25)
        alpha = np.random.uniform(0.05, 0.2)
        color = np.random.choice(['#306998', '#FFD43B', '#4B8BBE', '#646464', '#3776AB'])
        circle = Circle((x, y), r, facecolor=color, edgecolor='none', alpha=alpha)
        ax.add_patch(circle)

    # Connection lines (network effect)
    for _ in range(25):
        x1, y1 = np.random.uniform(1, 9), np.random.uniform(1, 7)
        x2, y2 = x1 + np.random.uniform(-2, 2), y1 + np.random.uniform(-1.5, 1.5)
        ax.plot([x1, x2], [y1, y2], color='#4B8BBE', alpha=0.08, linewidth=0.8)

    # Central Python logo-inspired shape
    for i in range(3):
        r = 1.8 - i * 0.4
        alpha = 0.12 + i * 0.05
        circle = Circle((5.12, 4.2), r, facecolor='#306998', edgecolor='#FFD43B',
                        alpha=alpha, linewidth=1.5)
        ax.add_patch(circle)

    # Title text
    ax.text(5.12, 4.6, 'Python', fontsize=52, fontweight='bold',
            color='#FFD43B', ha='center', va='center',
            fontfamily='sans-serif', alpha=0.95)
    ax.text(5.12, 3.7, 'Turns 35', fontsize=36, fontweight='light',
            color='#ffffff', ha='center', va='center',
            fontfamily='sans-serif', alpha=0.85)
    ax.text(5.12, 2.9, '1991  -  2026', fontsize=18,
            color='#4B8BBE', ha='center', va='center',
            fontfamily='sans-serif', alpha=0.7)

    ax.set_xlim(0, 10.24)
    ax.set_ylim(0, 7.68)
    ax.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(f"{output_dir}/featured-python-35.png", dpi=100,
                bbox_inches='tight', pad_inches=0, facecolor='#0d1117')
    plt.close()
    print("Created: featured-python-35.png")


def timeline_phases():
    """Create a clean timeline of Python's 4 phases -- tight layout, no wasted space."""
    fig, ax = plt.subplots(figsize=(10.24, 6.4), dpi=100)
    fig.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')

    phases = [
        {"year": "1991-2000", "title": "Scripting & Academia",
         "color": "#306998", "y": 5.2,
         "desc": "Teaching language\nUnix scripting\nReadable syntax"},
        {"year": "2000-2010", "title": "Web & Open Source",
         "color": "#4B8BBE", "y": 3.8,
         "desc": "Django & Flask\nStartup adoption\nLinux ecosystem"},
        {"year": "2010-2020", "title": "Data Science & AI",
         "color": "#FFD43B", "y": 2.4,
         "desc": "NumPy, Pandas\nTensorFlow, PyTorch\nJupyter Notebooks"},
        {"year": "2020-2026", "title": "Platform & Cloud",
         "color": "#e8584a", "y": 1.0,
         "desc": "FastAPI\nAI orchestration\nUniversal glue"},
    ]

    # Title
    ax.text(5.12, 6.1, "Python's Evolution: Four Phases", fontsize=24,
            fontweight='bold', color='#ffffff', ha='center',
            fontfamily='sans-serif', alpha=0.95)

    # Central timeline line
    ax.plot([2.0, 2.0], [0.4, 5.8], color='#4B8BBE', linewidth=3, alpha=0.4)

    for p in phases:
        # Phase dot
        circle = Circle((2.0, p["y"]), 0.16, facecolor=p["color"],
                        edgecolor='#ffffff', linewidth=2, alpha=0.9, zorder=5)
        ax.add_patch(circle)

        # Year label (left)
        ax.text(1.4, p["y"], p["year"], fontsize=13, fontweight='bold',
                color=p["color"], ha='right', va='center',
                fontfamily='sans-serif')

        # Phase box
        box = FancyBboxPatch((2.8, p["y"] - 0.5), 6.5, 1.0,
                            boxstyle="round,pad=0.12",
                            facecolor=p["color"], alpha=0.15,
                            edgecolor=p["color"], linewidth=1.5)
        ax.add_patch(box)

        # Phase title
        ax.text(3.1, p["y"] + 0.25, p["title"], fontsize=16,
                fontweight='bold', color=p["color"],
                fontfamily='sans-serif')

        # Phase description
        ax.text(3.1, p["y"] + 0.0, p["desc"], fontsize=10,
                color='#c9d1d9', fontfamily='sans-serif',
                va='top', linespacing=1.15)

    ax.set_xlim(0, 10.24)
    ax.set_ylim(0, 6.4)
    ax.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(f"{output_dir}/python-phases-timeline.png", dpi=100,
                bbox_inches='tight', pad_inches=0.15, facecolor='#0d1117')
    plt.close()
    print("Created: python-phases-timeline.png")


def python_vs_java():
    """Create a modern comparison graphic: Python vs Java."""
    fig, ax = plt.subplots(figsize=(10.24, 7.68), dpi=100)
    fig.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')

    # Title
    ax.text(5.12, 7.2, "Python at 35  vs  Java at 30", fontsize=24,
            fontweight='bold', color='#ffffff', ha='center',
            fontfamily='sans-serif')
    ax.text(5.12, 6.7, "Two complementary visions of software engineering",
            fontsize=13, color='#8b949e', ha='center',
            fontfamily='sans-serif')

    categories = [
        "Developer Speed",
        "AI & ML",
        "Enterprise Safety",
        "Performance",
        "Concurrency",
        "Learning Curve",
        "Ecosystem Maturity",
    ]
    python_scores = [9.5, 9.5, 5.0, 5.5, 5.0, 9.0, 8.5]
    java_scores =   [6.0, 3.5, 9.0, 8.5, 9.0, 5.5, 9.5]

    y_positions = np.linspace(5.8, 1.0, len(categories))
    bar_height = 0.32
    max_bar_width = 3.2

    for i, (cat, ps, js) in enumerate(zip(categories, python_scores, java_scores)):
        y = y_positions[i]

        # Category label
        ax.text(5.12, y + 0.35, cat, fontsize=12, fontweight='bold',
                color='#c9d1d9', ha='center', fontfamily='sans-serif')

        # Python bar (left from center)
        pw = (ps / 10) * max_bar_width
        python_bar = FancyBboxPatch((5.05 - pw, y - bar_height/2), pw, bar_height,
                                   boxstyle="round,pad=0.03",
                                   facecolor='#306998', alpha=0.8,
                                   edgecolor='none')
        ax.add_patch(python_bar)

        # Java bar (right from center)
        jw = (js / 10) * max_bar_width
        java_bar = FancyBboxPatch((5.19, y - bar_height/2), jw, bar_height,
                                 boxstyle="round,pad=0.03",
                                 facecolor='#e8584a', alpha=0.8,
                                 edgecolor='none')
        ax.add_patch(java_bar)

        # Center divider
        ax.plot([5.12, 5.12], [y - 0.2, y + 0.2], color='#30363d',
                linewidth=1, alpha=0.5)

    # Legend
    python_patch = mpatches.Patch(color='#306998', label='Python (35 yrs)')
    java_patch = mpatches.Patch(color='#e8584a', label='Java (30 yrs)')
    legend = ax.legend(handles=[python_patch, java_patch], loc='lower center',
                      ncol=2, fontsize=12, frameon=False,
                      bbox_to_anchor=(0.5, -0.02))
    for text in legend.get_texts():
        text.set_color('#c9d1d9')

    # Taglines
    ax.text(2.0, 0.3, "Optimized for humans", fontsize=11, color='#306998',
            ha='center', fontfamily='sans-serif', style='italic', alpha=0.8)
    ax.text(8.2, 0.3, "Optimized for systems", fontsize=11, color='#e8584a',
            ha='center', fontfamily='sans-serif', style='italic', alpha=0.8)

    ax.set_xlim(0, 10.24)
    ax.set_ylim(0, 7.68)
    ax.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(f"{output_dir}/python-vs-java-comparison.png", dpi=100,
                bbox_inches='tight', pad_inches=0.2, facecolor='#0d1117')
    plt.close()
    print("Created: python-vs-java-comparison.png")


if __name__ == "__main__":
    featured_image()
    timeline_phases()
    python_vs_java()
    print("\nAll images generated successfully!")
