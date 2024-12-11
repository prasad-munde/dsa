#include <iostream>
#define MAX 10

using namespace std;

struct QueueData {
    int data[MAX];
    int front, rear;
};

class Queue {
    QueueData q;
public:
    Queue() { 
        q.front = q.rear = -1; 
    }
    bool isempty();
    bool is_full();
    void enqueue(int);
    int del_queue();
    void display();
};

bool Queue::isempty() {
    return (q.front == -1);
}

bool Queue::is_full() {
    return ((q.rear + 1) % MAX == q.front);
}

void Queue::enqueue(int value) {
    if (is_full()) {
        cout << "Queue is full. Cannot enqueue " << value << endl;
    } else {
        if (q.front == -1) { // Queue is initially empty
            q.front = 0;
        }
        q.rear = (q.rear + 1) % MAX;
        q.data[q.rear] = value;
    }
}

int Queue::del_queue() {
    if (isempty()) {
        cout << "Queue is empty. Cannot dequeue." << endl;
        return -1; // Assuming -1 indicates an error
    } else {
        int value = q.data[q.front];
        if (q.front == q.rear) { // Queue will be empty after this operation
            q.front = q.rear = -1;
        } else {
            q.front = (q.front + 1) % MAX;
        }
        return value;
    }
}

void Queue::display() {
    if (isempty()) {
        cout << "Queue is empty." << endl;
    } else {
        int i = q.front;
        cout << "Queue elements are: ";
        while (true) {
            cout << q.data[i] << " ";
            if (i == q.rear) break;
            i = (i + 1) % MAX;
        }
        cout << endl;
    }
}

int main() {
    Queue q;
    int choice, value;

    while (true) {
        cout << "\n----- Queue Menu -----\n";
        cout << "1. Enqueue\n";
        cout << "2. Dequeue\n";
        cout << "3. Display\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice) {
            case 1:
                cout << "Enter value to enqueue: ";
                cin >> value;
                q.enqueue(value);
                break;
            case 2:
                value = q.del_queue();
                if (value != -1) {
                    cout << "Dequeued value: " << value << endl;
                }
                break;
            case 3:
                q.display();
                break;
            case 4:
                cout << "Exiting..." << endl;
                return 0;
            default:
                cout << "Invalid choice. Please enter a number between 1 and 4." << endl;
                break;
        }
    }
    return 0;
}
