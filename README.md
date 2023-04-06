# atomic-orbital-with-quantum-number-

For visualizing the orbitals by using quantum numbers we need to solve wave equation and find the 
probabilities for different x-y-z in coordinate to find places that the probability of electron existence is higher
**Full hydrogen wave function:**
The hydrogen wave function has two part it contains radial part and spherical harmonic




![1](https://user-images.githubusercontent.com/90906907/230291283-0de57c6d-ce41-4ca7-b7c8-e53b2fbffd70.png)

**Spherical harmonic:**
In python we have a library that contains spherical harmonics I use that:

![Screenshot 2023-04-06 094937](https://user-images.githubusercontent.com/90906907/230291340-f14b2f77-6c5f-4c7e-bc8f-e69c9518c476.png)

this function take m , l , phi , theta :

![Screenshot 2023-04-06 094957](https://user-images.githubusercontent.com/90906907/230291354-884ec85f-180c-43f6-96ca-598ad4f4b5b0.png)

**the Radial wave function:**

![Screenshot 2023-04-06 095936](https://user-images.githubusercontent.com/90906907/230291378-1bd26a8c-1505-4c68-bad6-73cc95bc822e.png)

 This is the formula of radial part it contains an exponential equation and a laguerre polynomial


**Combining Radial and spherical harmonic in (def hydrogen_wf(n,l,m,X,Y,Z))**

This def give us the wave function, now by square wave function we have probability

![Screenshot 2023-04-06 100335](https://user-images.githubusercontent.com/90906907/230291440-16b3b47d-fdb2-4901-a147-b7b547c75d74.png)

**result:**


![Screenshot 2023-04-06 100414](https://user-images.githubusercontent.com/90906907/230291462-bbe85160-d8cb-4439-8796-26cd5891aa56.png)
