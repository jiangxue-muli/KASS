def query_by_id(user_id):
    print(f'查询 {user_id} User')

def query_by_name(user_name):
    print(f"查询: {user_name} User")

def main():
    while True:
        option = input('1.查询 User 2.查询 Name >')
        if option == '1':
            user_id = input('查询 User id>')
            query_by_id(user_id)
        elif option == '2':
            user_name = input('查询 Name:>')
            query_by_name(user_name)
        elif option == 'exit':
            print("退出")
            break
        else:
            print('Syntax error')

if __name__ == '__main__':
    main()

