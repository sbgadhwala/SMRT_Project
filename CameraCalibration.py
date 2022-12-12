import pandas as pd
from sklearn.linear_model import LinearRegression

def getCoords():
    train_df = pd.read_csv(r"/home/ise.ros/Shyam/Camera Data.csv")

    train_df['area2'] = train_df['area']**2
    train_df['center_x2'] = train_df['center_x']**2
    train_df['center_y2'] = train_df['center_y']**2
    train_df['center_x_area'] = train_df['center_x']*train_df['area']
    train_df['center_y_area'] = train_df['center_y']*train_df['area']


    train_y = train_df[['ros_x', 'ros_y']]
    train_x = train_df[['area', 'center_x', 'center_y', 'area2', 'center_x2', 'center_y2', 'center_x_area', 'center_y_area']]

    model = LinearRegression()

    model.fit(train_x, train_y)


    a = 0
    cx = 0
    cy = 0

    with open(r"/home/ise.ros/Shyam/center_x.txt") as f:
        cx = int(f.readline())

    with open(r"/home/ise.ros/Shyam/center_y.txt") as f:
        cy = int(f.readline())

    with open(r"/home/ise.ros/Shyam/area.txt") as f:
        a = int(f.readline())

    print(a)
    print(cx)
    print(cy)
    
    test_x = pd.DataFrame(list(zip([a], [cx], [cy], [a**2], [cx**2], [cy**2], [cx*a], [cy*a])), columns = ['area', 'center_x', 'center_y', 'area2', 'center_x2', 'center_y2', 'center_x_area', 'center_y_area'])
    print(model.predict(test_x))
    with open(r"/home/ise.ros/Shyam/current_pos.txt",'r+') as file:
        file.truncate(0)
                    
    file1 = open(r"/home/ise.ros/Shyam/current_pos.txt", "a")
    file1.write(str(model.predict(test_x)))
    file1.close()


if __name__ == "__main__":
    getCoords()