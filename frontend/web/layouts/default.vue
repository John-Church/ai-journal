<template>
  <div class="w-full h-screen font-serif">
    <div class="mx-auto flex justify-between max-w-7xl px-8 py-4 items-center">
      <h1 class="font-sans text-2xl font-bold">Mnemo</h1>
      <div class="space-x-8">
        <NuxtLink to="/">Record Journal</NuxtLink>
        <NuxtLink to="/entries">Entries</NuxtLink>
      </div>
    </div>
    <slot />
  </div>
</template>
