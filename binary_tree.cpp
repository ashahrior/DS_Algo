#include<bits/stdc++.h>
using namespace std;

struct BinaryTreeNode {
    int data;
    BinaryTreeNode *left;
    BinaryTreeNode *right;
    BinaryTreeNode() {

    }
    BinaryTreeNode(int val) {
        data = val;
        left = right = NULL;
    }
};

BinaryTreeNode* getNewNode(int data) {
    BinaryTreeNode *node = new BinaryTreeNode();

    node->data = data;
    node->left = node->right = NULL;

    return node;
}

BinaryTreeNode* insert(BinaryTreeNode *root, int data) {

    if(root==NULL) {
        root = new BinaryTreeNode(data);
        return root;
    }
    if(root->left==NULL) {
        root->left = new BinaryTreeNode(data);
        return root;
    }
    else if(root->right == NULL) {
        root->right = new BinaryTreeNode(data);
        return root;
    }
    if(root->left!=NULL) {
        root->left = insert(root->left, data);
        return root;
    }

    return root;
}

bool search(BinaryTreeNode *root, int data) {
    if(root == NULL) return false;

    if(root->data==data)
        return true;
    
    else if(root->left != NULL)
        return search(root->left, data);
    else
        return search(root->right, data);
}

void traverse(BinaryTreeNode *root) {
    if (root == NULL)
    {
        cout << "Empty" << endl;
        return;
    }
    cout << root->data << endl;
    traverse(root->left);
    traverse(root->right);

    return;
}


int main(int argc, char const *argv[])
{
    /* code */

    BinaryTreeNode *root = NULL;
    root = insert(root, 15);
    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 25);
    root = insert(root, 8);
    root = insert(root, 12);

    cout << search(root, 8) << endl;

    traverse(root);

    return 0;
}
