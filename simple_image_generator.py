from PIL import Image, ImageDraw, ImageFont
import os

# Function to create a slide
def create_slide(title, content, width=1280, height=720):
    # Create a blank white image
    slide = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(slide)
    
    # Define fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 60)
        content_font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        title_font = ImageFont.load_default()
        content_font = ImageFont.load_default()
    
    # Title coordinates and content coordinates
    title_coords = (50, 30)
    content_coords = (50, 150)
    
    # Draw the title and content on the slide
    draw.text(title_coords, title, fill="black", font=title_font)
    draw.multiline_text(content_coords, content, fill="black", font=content_font, spacing=10)
    
    return slide

# Slide content
slides_content = [
    ("ProxyProvider in Flutter", ""),
    ("What is ProxyProvider?", "ProxyProvider is a special provider in Flutter that allows you to depend on other providers and create new values based on their values.\n\nIt is part of the provider package, which is widely used for state management in Flutter applications."),
    ("Benefits of ProxyProvider", "1. Dependency Injection: Automatically updates when dependencies change.\n2. Reusability: Enhances modularity by reusing existing providers.\n3. Performance: Efficient updates reduce unnecessary rebuilds."),
    ("Advantages of ProxyProvider", "1. Simplifies State Management: Easy to manage state dependencies.\n2. Improves Code Readability: Clear separation of concerns.\n3. Reduces Boilerplate: Minimizes repetitive code."),
    ("When to Use ProxyProvider?", "Use ProxyProvider when:\n1. You need to create a value based on other providers.\n2. Dependencies among providers need to be dynamically updated.\n3. Multiple providers depend on a common resource."),
    ("Code Example", """import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        Provider<int>(create: (_) => 10),
        ProxyProvider<int, String>(
          update: (_, value, previous) => 'Value is $value',
        ),
      ],
      child: MaterialApp(
        home: Scaffold(
          appBar: AppBar(title: Text('ProxyProvider Example')),
          body: Center(
            child: ValueWidget(),
          ),
        ),
      ),
    );
  }
}

class ValueWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final value = Provider.of<String>(context);
    return Text(value);
  }
}"""),
    ("Conclusion", "ProxyProvider is a powerful tool in the Flutter provider package.\n\nIt simplifies complex state management scenarios by allowing dynamic dependency injection.\n\nLeveraging ProxyProvider can lead to more maintainable and efficient Flutter applications.")
]

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")


# Create slides
slides = [create_slide(title, content) for title, content in slides_content]

# Save slides
for i, slide in enumerate(slides):
    slide.save(os.path.join(desktop_path, f"slide_{i+1}.png"))
