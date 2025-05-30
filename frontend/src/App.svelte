<script>
  import Router from 'svelte-spa-router';
  import Home from './routes/Home.svelte';

  const routes = {
    '/': Home,
    // Add other routes here as needed
  };
</script>

<Router {routes} />
