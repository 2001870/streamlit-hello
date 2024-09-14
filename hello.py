import streamlit as st
import time  # 用于模拟延时

st.set_page_config(page_title='lover', page_icon="💌")

# 预定义的姓名列表
valid_names = ['唐悦媛', '葛青怡', '张雨萌', '居仕琪', '杨万兴', '赵吕聪', '刘莘', '周诣扬', '李瑞', '许志奥', '谷雨凡', '王其兰', '陈海军', '陈雯静','程之璇','徐葛薇蓉','邓雯欣']

# Streamlit 应用部分
if 'page' not in st.session_state:
    st.session_state.page = 'main'

if st.session_state.page == 'main':
    st.title('姓名输入')

    # 用户输入姓名
    name = st.text_input("请输入您的姓名")

    # 在点击按钮时显示加载图标
    if st.button('💞'):
        # 显示加载图标
        with st.spinner('🎑正在验证姓名...'):
            time.sleep(1)  # 模拟处理时间
            if name in valid_names:
                st.session_state.page = 'holiday'  # 设置状态为假日
            else:
                st.warning("姓名不在允许的列表中，请输入有效的姓名")

elif st.session_state.page == 'holiday':
    # 使用单列
    st.markdown(
        """
        <style>
        h1 {
            text-align: center;  /* 居中对齐 */
        }
        .gif-container {
            display: flex;
            justify-content: center;
        }
        .gif-container img {
            width: 300px;  /* 调整 GIF 动画的宽度 */
            height: auto;  /* 保持 GIF 动画的纵横比 */
        }
        .return-button {
            font-size: 20px;  /* 按钮字体大小 */
            position: absolute; /* 绝对定位 */
            top: 10px; /* 距离顶部 10px */
            left: 10px; /* 距离左侧 10px */
            padding: 10px 20px; /* 按钮内边距 */
            background-color: #f0e68c; /* 按钮背景色 */
            border: none; /* 无边框 */
            border-radius: 5px; /* 圆角 */
            cursor: pointer; /* 鼠标指针 */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 显示返回首页按钮
    if st.button('🥮 返回首页  🌕', key='return_button', help='点击返回首页'):
        st.session_state.page = 'main'

    # 标题
    st.markdown("<h1>中秋快乐🤗!!!</h1>", unsafe_allow_html=True)

    # 显示 GIF 图像并设置大小
    st.markdown(
        """
        <div class="gif-container">
            <img src="https://s1.aigei.com/src/img/gif/fa/fabc31dcc99640a6966cc71d846cbaeb.gif?e=1735488000&token=P7S2Xpzfz11vAkASLTkfHN7Fw-oOZBecqeJaxypL:Zglq0Yh533zZ3D-ggdX0g4BwyK0=">
        </div>
        """,
        unsafe_allow_html=True
    )
