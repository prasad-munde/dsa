#include<iostream>
#include<string.h>
using namespace std;
struct node 
{
    int prn, roll_no;
    char name[50];
    struct node *next;
};
class info 
{
    node *s = NULL, *head1 = NULL, *temp1 = NULL, *head2 = NULL, *temp2 = NULL,       *head = NULL, *temp = NULL;
    int b, c, i, j, ct;  
    char a[20];
    public:
    node *create();
    void insert_p();
    void insert_m();
    void del_m();
    void del_p();
    void del_s();
    void display();
    void count();
    void reverse();
    void rev(node *p);
    void concat();
};

node *info::create() 
{
    node *p = new(struct node);
    cout << "\nName of student: ";
    cin >> a;
    strcpy(p->name, a);
    cout << "PRN No.: ";
    cin >> b;
    p->prn = b;
    cout << "Roll No.: ";
    cin >> c;
    p->roll_no = c;
    p->next = NULL;
    return p;
}

void info::insert_m() 
{
    node *p = create();
    if (head == NULL)
    {
        head = p;
    }
    else 
    {
        temp = head;
        while (temp->next != NULL) { temp = temp->next; }
        temp->next = p;
    }
}

void info::insert_p() 
{
    node *p = create();
    if(head == NULL)
    {
        head = p;
    }
    else 
    {
        temp = head;
        head = p;
        head->next = temp->next;
    }
}

void info::display() 
{
    if (head == NULL) 
    {
        cout << "Linklist is Empty";
    }
    else 
    {
        temp = head;
        cout << "PRN No.\tRoll No.\tName" << endl;
        while (temp->next != NULL) 
        {
            cout << " " << temp->prn << "\t   " << temp->roll_no << "\t\t" << temp->name << endl;
            temp = temp->next;
        }
        cout << " " << temp->prn << "\t   " << temp->roll_no << "\t\t" << temp->name << endl;
    }
}

void info::del_m() 
{
    int m, f = 0;
    cout << "Enter PRN No.(of member whose wanna remove): ";
    cin >> m;
    temp = head;
    while (temp->next != NULL) 
    {
        if (temp->prn == m) 
        {
            s->next = temp->next;
            delete (temp);
            f = 1;
            cout << "\nRemoving Successful!!";
        }
        s = temp;
        temp = temp->next;
    }
    if (f == 0) 
    {
    cout << "\nRemoving Unsuccessful!!";
    }
}

void info::del_p()
{
    temp = head;
    head = head->next;
    delete (temp);
    cout << "Removing Successful!!" << endl;
}

void info::del_s() 
{
    temp = head;
    while (temp->next != NULL) 
    {
        s = temp;
        temp = temp->next;
        cout << "Removing Successful!!" << endl;
    }
    s->next = NULL;
    delete (temp);
}

void info::count() 
{
    temp = head;
    ct = 0;
    while (temp->next != NULL) 
    {
        temp = temp->next;
        ct++;
    }
    ct++;
    cout << "Count of members is: " << ct;
}

void info::reverse() 
{ 
    rev(head); 
}

void info::rev(node *temp) 
{
    if (temp == NULL) 
    { 
        return; 
    }
    else 
    { 
        rev(temp->next); 
    }
    cout << temp->prn << "\t   " << temp->roll_no << "\t\t" << temp->name << endl;
}

void info::concat() 
{
    int k, j;
    cout << "No. of Members in List 1: ";
    cin >> k;
    head = NULL;
    for (i = 0; i < k; i++) 
    {
        insert_m();
        head1 = head;
    }
    head = NULL;
    cout << "No. of Members in List 2: ";
    cin >> j;
    for (i = 0; i < j; i++) 
    {
        insert_m();
        head2 = head;
    }
    head = NULL;
    temp1 = head1;
    while (temp1->next != NULL) 
    { 
        temp1 = temp1->next; 
    }
    temp1->next = head2;
    temp2 = head1;
    cout << "PRN No.\tRoll No.\tName" << endl;
    while (temp2->next != NULL) 
    {
        cout << temp2->prn << "\t   " << temp2->roll_no << "\t\t" << temp2->name << endl;
        temp2 = temp2->next;
    }
    cout << temp2->prn << "\t   " << temp2->roll_no << "\t\t" << temp2->name << endl;
}


int main() 
{
    info s;
    int i;
    cout<< "Menu\n 1. Add President\n 2. Add Member\n 3. Add Secrets\n 4. Remove President\n 5. Remove Member\n 6. Remove Secretary\n 7. Fetch Data\n 8. Get Number of Members\n 9. Display Reverse of String\n10. Concatenate two strings" << endl;
    char ch;
    do 
    {
        cout << "Enter choice: ";
        cin >> i;
        switch (i) 
        {
            case 1:
                s.insert_p();
                break;
            case 2:
                s.insert_m();
                break;
            case 3:
                s.insert_m();
                break;
            case 4:
                s.del_p();
                break;
            case 5:
                s.del_m();
                break;
            case 6:
                s.del_s();
                break;
            case 7:
                s.display();
                break;
            case 8:
                s.count();
                break;
            case 9:
                cout << "\nPRN No.\t   Roll No.\tName" << endl;
                s.reverse();
                break;
            case 10:
                s.concat();
                break;
            default:
                cout << "\nUnknown Choice" << endl;
        }
        cout << "\nDo you want to continue(Y/N): ", cin >> ch, cout << endl;
    }
    while (ch == 'y' || ch == 'Y');
    cout << "Exiting...";
return 0;
}
