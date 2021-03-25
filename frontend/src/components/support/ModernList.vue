<template>
  <ul class="uk-list uk-list-large uk-margin-medium-top">
    <li v-for="(item, index) in items" :key="index">
      <a :href="item.ref" data-uk-scroll="duration: 400; offset: 140" class="hvr-forward uk-link">
        <span data-uk-icon="icon: arrow-right"></span> {{item.title}}
      </a>
    </li>
  </ul>
</template>

<script>
export default {
	name: 'ModernList',
	props: ['items']
};
</script>