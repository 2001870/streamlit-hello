#import streamlit as st
#import time
#st.write('# 陈雯静是大美女!!!')

#sex = st.text_input("sex","woman")

#age=st.number_input("Age",1,10,6)

#st.write(f'input sex is {sex},age is {age}')

#def mock_login(uname,pwd):
    #time.sleep(1)
    #return uname=='JACK'and pwd =='123'


#username=st.text_input('Username','JACK')
#password=st.text_input('Password','1234')
#if st.button('login'):
    #with st.spinner('loading..'):
      #login_result=mock_login(username,password)
      #text='登录成功' if login_result else'登录失败'
      #st.write(text)
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 生成一些示例数据
# 特征数据 (X) 和目标数据 (y)
X = np.array([[1], [2], [3], [4], [5]])  # 特征（自变量）
y = np.array([2, 4, 6, 8, 10])  # 目标（因变量）

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X, y)

# Streamlit 应用部分
st.title('简单线性回归模型部署')

# 用户输入
X_test = st.number_input("输入X的值来预测Y", min_value=0.0, max_value=10.0)

# 进行预测并展示结果
if st.button('预测'):
    y_pred = model.predict([[X_test]])
    st.write(f'预测的Y值为: {y_pred[0]}')

    # 可视化数据和回归线
    plt.scatter(X, y, color='blue', label='实际数据')
    plt.plot(X, model.predict(X), color='red', linewidth=2, label='回归线')
    plt.scatter(X_test, y_pred, color='green', label='预测点', s=100)
    plt.xlabel('特征')
    plt.ylabel('目标')
    plt.title('线性回归示例')
    plt.legend()

    # 显示图形
    st.pyplot(plt)














