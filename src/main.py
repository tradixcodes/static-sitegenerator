from textnode import TextType, TextNode

def main():
    node1 = TextNode("Hello World", TextType.BOLD, None)
    print(node1)
    node_2 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node_2)

if __name__ == "__main__":
    main()
