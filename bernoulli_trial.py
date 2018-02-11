import scipy.misc as scm

def bernoulli_trial_calc(n,k,p):
    """
    Parameter
    ----------------
    n : number of statistically independent Bernoulli traial
    k : the number of success
    p : probability of success

    Retrun
    ----------------
    Probability of this bernoulli traial
    """
    return scm.comb(n,k) * ((p) **k) * ((1-p)**(n-k))

class bernoulli_trial:
    """
    class of beroulli_traial requeires two parameter n,p for initilization.
    """

    def __init__(self,n,p):
        """
        Parameter:
        ----------------
        n : number of statistically indepent Bernoulli trial
        p : probabillity of success
        """
        self.n = n
        self.p = p

    def calc(self,klist):
        """
        Parameter:
        ----------------
        k : list of number of success
        """
        prob_list = []
        for suc_num in klist:
            prob_list.append(bernoulli_trial_calc(self.n,suc_num,self.p))

        return prob_list


if __name__ == '__main__':
    n = 3
    p = 1/3

    ber_trial = bernoulli_trial(n,p)
    klist = [0,1,2,3]
    probability_list = ber_trial.calc(klist)

    print(probability_list)
