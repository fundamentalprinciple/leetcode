/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define MAX_SIZE 10001

typedef struct {
    struct TreeNode* arr[MAX_SIZE];
    int top;
} Stack;

void initialize(Stack *stack) {
    stack->top = -1;
}

bool isEmpty(Stack *stack) {
    return stack->top == -1;
}

bool isFull(Stack *stack) {
    return stack->top >= MAX_SIZE-1;
}

void push(Stack *stack, struct TreeNode* node) {
    if (isFull(stack)) {
        printf("Stack if full!\n");
        return;
    }
    stack->arr[++stack->top] = node;
}

struct TreeNode* pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty!\n");
        return NULL;
    }
    struct TreeNode* popped = stack->arr[stack->top];
    stack->top--;
    return popped;
}

struct TreeNode* peek(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty!\n");
        return NULL;
    }
    return stack->arr[stack->top];
}

int maxDepth(struct TreeNode* root) {
    if(root==NULL) {
        return 0;
    }

    Stack stack;
    initialize(&stack);
    push(&stack, root);

    int depth = 1;
    int max_depth = 1;
    while(!isEmpty(&stack)) {
        struct TreeNode* top = peek(&stack);
        if(top->left!=NULL) {
            push(&stack, top->left);
            top->left=NULL;
            depth++;
        } else if(top->right!=NULL) {
            push(&stack, top->right);
            top->right=NULL;
            depth++;
        } else {
            pop(&stack);
            if(depth>max_depth) {
                max_depth=depth;
            }
            depth--;
        }
    }

    return max_depth;
}
