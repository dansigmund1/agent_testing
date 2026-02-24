from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        result = subprocess.run(
            ['python', 'scripts/check_setup.py'],
            capture_output=True,
            text=True,
            timeout=30
        )
        return jsonify({
            'status': 'success',
            'output': result.stdout,
            'errors': result.stderr
        })
    except subprocess.TimeoutExpired:
        return jsonify({'status': 'error', 'message': 'Script timed out'}), 500
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)