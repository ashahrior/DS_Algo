#include<bits/stdc++.h>
using namespace std;

struct BstNode {
    /* data */
    int data;
    BstNode *left;
    BstNode *right;

    BstNode() {}

    BstNode(int val) {
        data = val;
        left = right = NULL;
    }
};

BstNode* setNewNode(int data) {
    BstNode *node = new BstNode();
    node->data = data;
    node->left = node->right = NULL;
    return node;
}

BstNode* insert(BstNode *root, int data)
{
    if(root==NULL) {
        //root = getNewNode(data);
        root = new BstNode(data);
        return root;
    }
    else if(root->data > data) {
        root->left = insert(root->left, data);
    }
    else {
        root->right = insert(root->right, data);
    }
    return root;
}

bool search(BstNode *root ,int data) {
    if(root==NULL)
        return false;
    if(root->data == data)
        return true;
    if(root->data >= data)
        return search(root->left, data);
    else
        return search(root->right, data);
}

void traverse(BstNode *root) {

    if(root==NULL) {
        cout << "Empty" << endl;
        return;
    }
    cout << root->data << endl;
    traverse(root->left);
    traverse(root->right);

    return;
}


int main() {

    BstNode *root = NULL;
    root = insert(root,15);
    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 25);
    root = insert(root, 8);
    root = insert(root, 12);

    cout << search(root, 8) << endl;

    traverse(root);

    return 0;
}