import streamlit as st

# 设置网页标题和图标
st.set_page_config(page_title="爱心点餐台", page_icon="🍽️", layout="centered")
st.title("🍽️ 白姝专属爱心点餐台")

# 模拟菜品数据（不需要数据库）
menu = {
    "🥩 肉类": [
        {"name": "水煮肉片", "price": 9178, "desc": "麻辣鲜香", "id": 1},
        {"name": "回锅肉", "price": 9178, "desc": "肥瘦相间，香辣下饭", "id":2 },
        {"name": "麻辣香锅", "price": 9178, "desc": "荤素搭配，超下饭", "id":3 },
        {"name": "酸菜鱼（金汤/麻辣/花椒/清蒸）", "price": 9178, "desc": "开胃菜", "id": 4},
        {"name": "青椒肉丝", "price": 9178, "desc": "下饭一绝", "id":5 },
        {"name": "麻婆豆腐", "price": 9178, "desc": "下饭一绝", "id": 6},
        {"name": "蒜苔炒肉", "price": 9178, "desc": "下饭一绝", "id":7 },
        {"name": "小鸡炖蘑菇", "price": 9178, "desc": "下饭一绝", "id":8 },
        {"name": "木耳炒肉", "price":9178, "desc": "下饭一绝", "id":9 },
        {"name": "红烧肉", "price": 9178, "desc": "下饭一绝", "id": 10},
        {"name": "干锅鸭/虾[白灼]/鸡（红烧）", "price":9178, "desc": "下饭一绝", "id":11 },
        {"name": "火爆猪肝（腰花）", "price":9178, "desc": "下饭一绝", "id":12 },
        {"name": "番茄牛腩", "price":9178, "desc": "下饭一绝", "id":13 },
        {"name": "肉末茄子", "price":9178, "desc": "下饭一绝", "id":14 },
        {"name": "滑肉（原味/泡椒/番茄）", "price":9178, "desc": "下饭一绝", "id":15 },
        {"name": "白油肚条", "price":9178, "desc": "下饭一绝", "id":16 },
        {"name": "豆干炒肉", "price":9178, "desc": "下饭一绝", "id":17 },
        {"name": "可乐鸡翅", "price":9178, "desc": "下饭一绝", "id":18 },
        {"name": "蹄花汤", "price":9178, "desc": "下饭一绝", "id":19 },
        {"name": "蚂蚁上树", "price":9178, "desc": "下饭一绝", "id":20 },
        {"name": "梅菜扣肉", "price":9178, "desc": "下饭一绝", "id":21 },
        {"name": "蘑菇炒蛋", "price":9178, "desc": "鲜", "id":22 },
    ],
    "🥬 蔬菜": [
        {"name": "清炒时蔬", "price": 9178, "desc": "清爽解腻，健康首选", "id":23},
        {"name": "干煸四季豆", "price": 2778, "desc": "干香入味", "id":24},
        {"name": "豌豆尖汤", "price":9178, "desc": "鲜", "id":25},
        {"name": "番茄炒鸡蛋", "price":9178, "desc": "鲜", "id":26},
    ],
    "🍚 主食": [
        {"name": "爱心蛋炒饭/白米饭/面/稀饭/包子（包子只能有空多的时候）", "price": 2778, "desc": "吃晕碳", "id":27 },
        {"name": "龙肉", "price":9178, "desc": "鲜", "id":28},
    ]
}

# 初始化购物车（存在网页的临时内存里）
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'order_placed' not in st.session_state:
    st.session_state.order_placed = False

# 左侧边栏：购物车展示
with st.sidebar:
    st.header("🛒 她点的菜")
    if not st.session_state.cart:
        st.info("还没有点菜哦~")
    else:
        total_price = 0
        for item in st.session_state.cart:
            st.write(f"✅ {item['name']} - ￥{item['price']}")
            total_price += item['price']

        st.markdown(f"### 总计：￥{total_price:.2f}")

        # 下单按钮
        if st.button("❤️ 确认下单", type="primary", use_container_width=True):
            st.session_state.order_placed = True
            st.session_state.final_order = list(st.session_state.cart)  # 保存最终订单
            st.session_state.cart = []  # 清空购物车

# 主界面：展示菜单
if st.session_state.order_placed:
    st.balloons()  # 撒花特效
    st.success("🎉 下单成功！这就去给你做！")
    st.markdown("### 📝 订单详情：")
    total = 0
    for item in st.session_state.final_order:
        st.write(f"- **{item['name']}** x 1 （￥{item['price']}）")
        total += item['price']
    st.markdown(f"**合计金额：￥{total:.2f}**")

    if st.button("重新点单"):
        st.session_state.order_placed = False
        st.rerun()

else:
    # 按照分类展示菜品
    for category, items in menu.items():
        st.subheader(category)
        for item in items:
            # 使用卡片样式
            with st.container(border=True):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{item['name']}**  ￥{item['price']}")
                    st.caption(item['desc'])
                with col2:
                    # 加入购物车按钮
                    if st.button("➕ 加入", key=item['id']):
                        st.session_state.cart.append(item)
                        st.toast(f"已添加：{item['name']}")#streamlit run 点菜.py
