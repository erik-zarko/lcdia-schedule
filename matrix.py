import numpy as np
import itertools

class User:
    new_id = itertools.count()
    def __init__(self, matrix = None):
        if matrix is None:
            matrix = np.ones((12, 5))
        else:
            matrix = matrix
        self.id = next(User.new_id)
        self.matrix = matrix.copy()

class Scheduler:
    def schedule(self, user, xy):
        if user.matrix[xy[0], xy[1]] == 1:
            user.matrix[xy[0], xy[1]] = 0
        else:
            print(f'Horário não está disponível.')

    def cancel(self, user, xy):
        if user.matrix[xy[0], xy[1]] == 0:
            user.matrix[xy[0], xy[1]] = 1
        else:
            print(f'O usuário não possui compromisso marcado neste dia')

    def possible_meeting_days(self, users_list):
        users_matrix = np.stack([user.matrix for user in users_list])
        sum_matrix = np.sum(users_matrix, axis=0)

        max = np.max(sum_matrix)
        print(f'Numero maximo de participantes: {max}')
        max_idx = np.where(sum_matrix == max)

        return list(zip(max_idx[0], max_idx[1]))
    
class GetData:
    def import_schedule(self, path):
        return np.genfromtxt(path, delimiter=',')
        
