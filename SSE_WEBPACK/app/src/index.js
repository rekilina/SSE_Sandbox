import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';

const App = () => {
	const [data, setData] = useState('');

	useEffect(() => {
		const eventSource = new EventSource('http://localhost:5000/stream');
		// const eventSource = new EventSource('/stream');

		eventSource.onmessage = (event) => {
			console.log("onmessage", event.data);
			setData(event.data);
		};
		
		eventSource.onopen = () => {
			console.log("onopen");
		};

		eventSource.onclose = () => {
			console.log("closed!");
		};

		eventSource.onerror = () => {
			console.log("error!");

			eventSource.close();
		};

		return () => {
			eventSource.close();
		};
	}, []);

	return (
		<div>
			<h1>Server-Sent Events Demo</h1>
			<p>Data from server: {data}</p>
		</div>
	);
};

ReactDOM.render(<App />, document.getElementById('root'));
