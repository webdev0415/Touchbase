<template>
  <article class="uk-article uk-margin-xlarge-top">
    <h2 class="uk-article-title uk-margin-medium-bottom">
      {{title}}
      <a
        href="#"
        data-uk-totop
        data-uk-scroll="duration: 400"
        class="tm-totop uk-float-right uk-link uk-margin-small-top"
      ></a>
    </h2>
    <slot></slot>
  </article>
</template>

<script>
export default {
  name: "ArticleComponent", // cannot name it to Article because that will conflict with the HTML article tag
  props: ["title"]
};
</script>