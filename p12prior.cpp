#include <iostream>
using namespace std;

int f = 0, r = -1;

template<class T>
class priorityQ{
public:
    T arr[100];
    void push(T x);
    T pop();
    void show();
};

template<class T>
void priorityQ<T>::push(T x){
    if (r >= 99){
        cout<<"Overload!"<<endl;
    }
    else{
        r++;
        arr[r] = x;
    }
}

template<class T>
T priorityQ<T>::pop(){
    if (f > r){
        cout<<"Empty queue!"<< endl;
        return '\0';  // Explicitly return null character
    }
    else{
        T p = arr[f];
        f++;
        return p;
    }
}

template<class T>
void priorityQ<T>::show(){
    if (f > r){
        cout<<"Queue is empty";
    }
    else{
        for (int i = f; i <= r; i++){ // Start from f
            cout<<'\n'<< arr[i];
        }
    }
}

int main(){
    char jobID[10], conpop;
    int priorityID[10], n;

    priorityQ<char> JobQ;

    cout<<"Enter the number of jobs (max 10): ";
    cin >> n;

    if (n > 10) {
        cout << "Too many jobs. Maximum is 10.\n";
        return 1;
    }

    for (int i = 0; i < n; i++) {
    cout << "Enter job ID: ";
    cin >> jobID[i];
    cin.ignore(); // Clear the newline character from the buffer

    cout << "Enter job priority: ";
    cin >> priorityID[i];
    }


    // Sorting jobs by priority
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            if(priorityID[i] < priorityID[j]){
                swap(priorityID[i], priorityID[j]);
                swap(jobID[i], jobID[j]);
            }
        }
    }

    // Adding jobs to the priority queue
    for(int i = 0; i < n; i++){
        cout<<"\nJob ID: "<<jobID[i];
        cout<<"\nJob priority: "<< priorityID[i];
        JobQ.push(jobID[i]);
    }

    // Popping jobs from the queue
    conpop = 'Y';
    while(conpop == 'Y'||conpop == 'y'){
        if (f > r) {  // If queue is empty
            cout << "\nQueue is empty. Cannot pop more jobs.\n";
            break;
        }

        char popped = JobQ.pop();
        if (popped != '\0'){
            cout<<"\nPopped job: "<< popped;
        }

        cout << "\nDo you want to pop another job? (Y/N): ";
        cin >> conpop;
    }

    // Display remaining jobs
    cout << "\nContents of queue: ";
    JobQ.show();

    return 0;
}