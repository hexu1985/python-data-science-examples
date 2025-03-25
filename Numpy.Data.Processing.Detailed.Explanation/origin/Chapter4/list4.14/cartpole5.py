import gym
import numpy as np
import matplotlib.pyplot as plt

def do_episode(w, env):
    done = False
    observation = env.reset()
    num_steps = 0

    while not done and num_steps <= max_number_of_steps:
        action = take_action(observation, w)
        observation, _, done, _ = env.step(action)
        num_steps += 1
    #  在这里给与报酬，简单的说就是将（连续完成的步数-最大步数)作为报酬给予
    step_val = -1 if num_steps >= max_number_of_steps else num_steps - max_number_of_steps
    return step_val, num_steps

#如果值超过0，就返回1
def take_action(X, w): 
    action = 1 if calculate(X, w) > 0.0 else 0
    return action

def calculate(X, w):
    # 返回值不是数组，而是一个数值
    result = np.dot(X, w) 
    return result

env = gym.make('CartPole-v0')

# env.render()
# 如果需要观察游戏的状态，则执行env.render()语句即可

eta = 0.2
#  更新参数用的标准差
sigma = 0.05 

#  进行学习的最大对局数
max_episodes = 5000 
max_number_of_steps = 200
# 输入的参数数量
n_states = 4 
num_batch = 10

# 评估范围内的对局数
num_consecutive_iterations = 100 

w = np.random.randn(n_states)
reward_list = np.zeros(num_batch)
last_time_steps = np.zeros(num_consecutive_iterations)
#  记录过去100次对局中完成的步数的平均值作为学习进度信息
mean_list = [] 

for episode in range(max_episodes//num_batch):
    N = np.random.normal(scale=sigma,size=(num_batch, w.shape[0]))
    #  用于修改参数值的值，这个是误差值
    for i in range(num_batch):
        w_try = w + N[i]
        reward, steps = do_episode(w_try, env)
        if i == num_batch-1:
            print('%d Episode finished after %d steps / mean %f' %(episode*num_batch, steps, last_time_steps.mean()))
        last_time_steps = np.hstack((last_time_steps[1:], [steps]))
        reward_list[i] = reward
        mean_list.append(last_time_steps.mean())
    #  平均步数超过195就停止学习
    if last_time_steps.mean() >= 195: break 

    std = np.std(reward_list)
    if std == 0: std = 1
    # 对报酬值进行归一化处理
    A = (reward_list - np.mean(reward_list))/std
    #  在这里对参数进行更新
    w_delta = eta /(num_batch*sigma) * np.dot(N.T, A)
    #  乘以sigma用于调整幅度
    w += w_delta


env.close()

#  绘制并显示图表
plt.plot(mean_list)
plt.xlabel("episode")
plt.ylabel("mean_step")
plt.show()