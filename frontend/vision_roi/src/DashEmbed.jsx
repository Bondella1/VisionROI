import React from 'react';

const DashEmbed = () => (
  <div style={{ width: '100%', height: '600px' }}>
    <iframe
      src="http://localhost:8000/dash"
      style={{ width: '100%', height: '100%', border: 'none' }}
      title="ROI Calculator Dashboard"
    />
  </div>
);

export default DashEmbed;
