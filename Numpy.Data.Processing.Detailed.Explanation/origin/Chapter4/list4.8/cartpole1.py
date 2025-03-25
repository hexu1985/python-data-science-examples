q_table = np.random.uniform(low=-1, high=1, size=(4 ** 4, env.action_space.n))

def bins(clip_min, clip_max, num):
    return np.linspace(clip_min, clip_max, num + 1)[1:-1]

def digitize_state(observation):
    # 将各个值转换为4个离散值
    cart_pos, cart_v, pole_angle, pole_v = observation
    digitized = [np.digitize(cart_pos, bins=bins(-2.4, 2.4, 4)),
                 np.digitize(cart_v, bins=bins(-3.0, 3.0, 4)),
                 np.digitize(pole_angle, bins=bins(-0.5, 0.5, 4)),
                 np.digitize(pole_v, bins=bins(-2.0, 2.0, 4))]
    # 转换为0～255的数
    return sum([x * (4 ** i) for i, x in enumerate(digitized)])
