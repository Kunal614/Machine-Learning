# One Hidden Neural Network

![Neural Network](https://github.com/Kunal614/Machine-Learning/blob/master/neural_network/classification_kiank.png)

Mathematically:

                                                For one example x(i):
                                                z[1](i) = W[1] x(i) + b[1]
                                                z[1](i) = W[1] x(i) + b[1]
                                                a[1](i) = tanh(z[1](i))(2)
                                                a[1](i) = tanh⁡(z[1](i))
                                                z[2](i) = W[2]a[1](i) + b[2](3)
                                                z[2](i) = W[2]a[1](i) + b[2]
                                                ŷ (i) = a[2](i) = σ(z[2](i))(4)
                                                y^(i) = a[2](i) = σ(z[2](i))
                                                y(i)prediction={10if a[2](i)>0.5otherwise (5)
                                                yprediction(i)={1if a[2](i)>0.50otherwise

Given the predictions on all the examples, you can also compute the cost JJ as follows:\
J=−1m∑i=0m(y(i)log(a[2](i))+(1−y(i))log(1−a[2](i)))(6)\
J=−1m∑i=0m(y(i)log⁡(a[2](i))+(1−y(i))log⁡(1−a[2](i)))

Reminder: The general methodology to build a Neural Network is to:

1. Define the neural network structure ( # of input units,  # of hidden units, etc). 
2. Initialize the model's parameters
3. Loop:
    - Implement forward propagation
    - Compute loss
    - Implement backward propagation to get the gradients
    - Update parameters (gradient descent)


# Backward Propagation Formula
![Backward Propagation](https://github.com/Kunal614/Machine-Learning/blob/master/neural_network/grad_summary.png)
