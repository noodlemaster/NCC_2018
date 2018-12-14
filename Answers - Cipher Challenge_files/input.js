(function($){var doingLink='';var modal_bound=false;function trap_events(event){if(typeof event.preventDefault!='undefined')
{event.preventDefault();}
else
{event.returnValue=false;}
event.stopPropagation();}
function get_postid(url,field_id){if(!$('#'+field_id+'-postid').length){return;}
var ajax_data={'action':'link_picker_postid_lookup','url':url,'field_id':field_id};$.post(ajaxurl,ajax_data,function(response){var post_id=response.post_id;var id=response.field_id;if($('#'+id+'-postid').length&&$('#'+id+'-postid-label').length){$('#'+id+'-postid').val(post_id);$('#'+id+'-postid-label').html(post_id);}},'json');}
function initialize_field($el){$el.on('click','.acf-lp-link-btn, .acf-label label',function(event)
{trap_events(event);var thisID;if($(this).is('label')){thisID='link-picker-'+$(this).attr('for');}else{thisID=$(this).attr("id");}
doingLink=thisID;if(typeof wpLink!=='undefined'){var current_url=$('#'+doingLink+'-url').val();var current_title=$('#'+doingLink+'-title').val();var current_target=$('#'+doingLink+'-target').val();wplink_defaults=wpLink.setDefaultValues;wpLink.setDefaultValues=function(){$('#wp-link-text').val(current_title);$('#wp-link-url').val(current_url);$('#wp-link-target').prop('checked',(current_target==='_blank'));$('#wp-link-search').val('');};wpLink.open(thisID);}
return false;});$el.on('click','.acf-lp-link-remove-btn',function(event)
{var thisID=$(this).attr("id").replace("-remove","");doingLink=thisID;$('#'+doingLink+'-url').val('');$('#'+doingLink+'-title').val('');$('#'+doingLink+'-target').val('');if($('#'+doingLink+'-postid').length){$('#'+doingLink+'-postid').val('');}
$('#'+doingLink+'-none').show();$('#'+doingLink+'-exists').hide();if(typeof acf._e!='undefined')
{$('#'+doingLink).html(acf._e('link_picker','insert_link'));}
else
{$('#'+doingLink).html(translations.insert_link);}
$('#'+doingLink+'-remove').fadeOut('fast');trap_events(event);return false;});if(!modal_bound){bind_wplink_handlers();modal_bound=true;}
var url=$el.find('input[name$="[url]"]').val();if(url){var $postid_input=$el.find('input[name$="[postid]"]');if($postid_input.length){var post_id=$postid_input.val();if(!post_id||post_id==0){get_postid(url,$postid_input.attr('id').replace('-postid',''));}}}}
function reset_wplink(){wpLink.textarea=$('body');wpLink.close();wpLink.setDefaultValues=wplink_defaults;doingLink='';}
function bind_wplink_handlers(){$('body').on('click','#wp-link-submit',function(event)
{if(doingLink!=='')
{var linkAtts=wpLink.getAttrs();if(!('title'in linkAtts)){linkAtts.title=$("#wp-link-text").val();}
$('#'+doingLink+'-url').val(linkAtts.href);$('#'+doingLink+'-title').val(linkAtts.title);$('#'+doingLink+'-target').val(linkAtts.target);$('#'+doingLink+'-url-label').html('<a href="'+linkAtts.href+'" target="_blank">'+linkAtts.href+'</a>');$('#'+doingLink+'-title-label').html(linkAtts.title);if(typeof acf._e!='undefined')
{$('#'+doingLink+'-target-label').html((linkAtts.target=='_blank')?acf._e('link_picker','yes'):acf._e('link_picker','no'));}
else
{$('#'+doingLink+'-target-label').html((linkAtts.target=='_blank')?translations.yes:translations.no);}
$('#'+doingLink+'-none').hide();$('#'+doingLink+'-exists').show();if(typeof acf._e!='undefined')
{$('#'+doingLink).html(acf._e('link_picker','edit_link'));}
else
{$('#'+doingLink).html(translations.edit_link);}
$('#'+doingLink+'-remove').fadeIn('fast');trap_events(event);reset_wplink();return false;}});$('body').on('click','#search-panel .query-results li',function(event)
{if(doingLink!=='')
{$('#wp-link-text').val($(this).find('.item-title').text());get_postid($(this).find('input.item-permalink').val(),doingLink);}});$('body').on('click','#wp-link-close, #wp-link-cancel a',function(event)
{if(doingLink!=='')
{trap_events(event);reset_wplink();return false;}});}
if(typeof acf.add_action!=='undefined'){acf.add_action('ready append',function($el){acf.get_fields({type:'link_picker'},$el).each(function(){initialize_field($(this));});});}else{$(document).live('acf/setup_fields',function(e,postbox){$(postbox).find('.field[data-field_type="link_picker"]').each(function(){initialize_field($(this));});});}})(jQuery);