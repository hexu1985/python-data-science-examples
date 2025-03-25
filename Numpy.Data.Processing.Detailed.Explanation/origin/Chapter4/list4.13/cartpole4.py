# coding: utf-8
import gym # 导入gym和NumPy模块
import numpy as np

#  将相当于环境的对象保存到env中
env = gym.make('CartPole-v0')

# 目标是保持连续195步以上棒子不倒
goal_average_steps = 195
# 最大步数
max_number_of_steps = 200
# 评估范围的对局数
num_consecutive_iterations = 100
num_episodes = 5000
last_time_steps = np.zeros(num_consecutive_iterations)

# 创建用于保存价值函数的输出值的表格
# np.random.uniform返回指定范围内的均匀分布的随机数
q_table = np.random.uniform(low=-1, high=1, size=(4**4, env.action_space.n))

def bins(clip_min, clip_max, num):
    # np.linspace返回指定范围内的等间距数列
    return np.linspace(clip_min, clip_max, num + 1)[1:-1]

def digitize_state(observation):
    # 将各个值转换为4个离散值
    #  np.digitize是将指定的数值归类到bins所指定的基数的函数。返回的是基数的索引
    cart_pos, cart_v, pole_angle, pole_v=observation
    digitized = [np.digitize(cart_pos, bins=bins(-2.4, 2.4, 4)),
                 np.digitize(cart_v, bins=bins(-3.0, 3.0, 4)),
                 np.digitize(pole_angle, bins=bins(-0.5, 0.5, 4)),
                 np.digitize(pole_v, bins=bins(-2.0, 2.0, 4))]
    #  转换为0～255的数

    #  可以使用带索引的循环语句
    return sum([x* (4**i) for i, x in enumerate(digitized)])

def get_action(state, action, observation, reward, episode):
    next_state = digitize_state(observation)

    epsilon = 0.5 * (0.99** episode)
   # 如果均匀随机数比0.2还要大
    if epsilon <= np.random.uniform(0, 1):
       # 将q_table中下一次所采取的行动当中具有最高价值的行动保存到next_action中
        next_action = np.argmax(q_table[next_state])
    else:
    # 换言之就是按照20%的概率随机采取行动
        next_action = np.random.choice([0, 1])


    #  更新Q表格
    alpha = 0.2
    gamma = 0.99
    q_table[state, action] = (1 - alpha) * q_table[state, action] + \
        alpha * (reward + gamma * q_table[next_state, next_action])
    return next_action, next_state

step_list = []
for episode in range(num_episodes):
    #  环境的初始化
    observation = env.reset()

    state = digitize_state(observation)
    action = np.argmax(q_table[state])

    episode_reward = 0
    for t in range(max_number_of_steps):
        # 绘制CartPole
        env.render()

        # 采取action时的环境、报酬、游戏状态是否为结束、调试信息等有用的信息
        observation, reward, done, info=env.step(action)
        # 添加棒子倒下时的惩罚项
        if done:
            reward -= 200
        #  选择下一个行动
        action, state = get_action(state, action, observation, reward, episode)
        episode_reward += reward

        if done:
            print('%d Episode finished after %f time steps / mean %f' %(episode, t + 1, last_time_steps.mean()))
            last_time_steps = np.hstack((last_time_steps[1:], [t+1]))
            #  将持续的步数保存到步数列表的最后。np.hstack是用于连接数组的函数
            step_list.append(last_time_steps.mean())
            break
    #  如果最近的100次记录达到195以上，就说明学习成功了
    if (last_time_steps.mean() >= goal_average_steps):
        print('Episode %d train agent successfully!' % episode)
        break

# 下面是绘制图表的代码
import matplotlib.pyplot as plt
plt.plot(step_list)
plt.xlabel('episode')
plt.ylabel('mean_step')
plt.show()