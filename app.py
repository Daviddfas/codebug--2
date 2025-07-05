import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide") # 设置页面布局为宽屏

st.title("Streamlit 中的动态可拖拽图")

st.write("""
这个示例展示了如何在 Streamlit 应用中嵌入一个使用 `vis.js` 创建的交互式、可拖拽的动态图。
您可以尝试拖拽图中的节点，它们会根据物理引擎的设定进行移动和重新布局。
""")

# 读取 HTML 文件内容
try:
    with open("graph.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # 使用 components.html 嵌入 HTML 代码
    # height 参数可以根据需要调整，确保图表有足够的空间显示
    components.html(html_code, height=650, scrolling=False)

except FileNotFoundError:
    st.error("找不到 'graph.html' 文件。请确保 'graph.html' 文件与 'app.py' 在同一目录下。")
except Exception as e:
    st.error(f"加载 HTML 时发生错误: {e}")

st.write("---")
st.info("Vis.js 是一个强大的网络图可视化库，支持多种交互功能。")