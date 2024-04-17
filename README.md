<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KD 3198 Stats Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f8f9fa;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #007bff;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
        }
        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border: 1px solid #dee2e6;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>KD 3198 Stats Dashboard</h1>
        <p>This project is a Streamlit-based dashboard for visualizing and analyzing player statistics from the game Kingdom 3198. It provides insights into player performance, including total kills, T4 and T5 kills, and dead troops, organized by KvK (Kingdom vs. Kingdom) events.</p>

        <h2>Features</h2>
        <ul>
            <li><strong>Performance Breakdown:</strong> Analyze player performance by total kills, T4 and T5 kills, and dead troops.</li>
            <li><strong>Data & Stats Tracking:</strong> Track and visualize player statistics to gain insights into performance trends over time.</li>
            <li><strong>Interactive Visualizations:</strong> Utilizes interactive charts and graphs powered by Plotly and Matplotlib for dynamic data exploration.</li>
        </ul>

        <h2>Usage</h2>
        <p>To use this dashboard:</p>
        <ol>
            <li><strong>Install Dependencies:</strong> Install the required dependencies listed in <code>requirements.txt</code>.</li>
            <li><strong>Access Data File:</strong> Ensure you have access to the necessary data file, <code>merged.xlsx</code>, containing player statistics.</li>
            <li><strong>Run Streamlit App:</strong> Run the Streamlit app by executing the following command in your terminal:</li>
        </ol>
        <pre><code>streamlit run app.py</code></pre>

        <h2>Dependencies</h2>
        <ul>
            <li>Streamlit</li>
            <li>Pandas</li>
            <li>NumPy</li>
            <li>Matplotlib</li>
            <li>Plotly</li>
        </ul>

        <h2>Contributing</h2>
        <p>Contributions to improve and extend this dashboard are welcome! If you find any bugs, have feature requests, or want to contribute enhancements, feel free to open an issue or submit a pull request.</p>

        <h2>License</h2>
        <p>This project is licensed under the MIT License.</p>
    </div>
</body>
</html>
